import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Receipt, ReceiptFile
from .serializers import ReceiptSerializer
from dateutil import parser as dateparser 


class ReceiptUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided'}, status=400)

        if not file.name.endswith('.pdf'):
            return Response({'error': 'Only PDF files are allowed'}, status=400)

        receipt_file = ReceiptFile.objects.create(file=file)
        return Response({'id': receipt_file.id, 'message': 'File uploaded successfully'}, status=201)
      
          

class ReceiptValidationView(APIView):
    def post(self, request):
        receipt_id = request.data.get('id')
        try:
            receipt_file = ReceiptFile.objects.get(id=receipt_id)
        except ReceiptFile.DoesNotExist:
            return Response({'error': 'Invalid receipt ID'}, status=404)

        if not receipt_file.file.name.endswith('.pdf'):
            receipt_file.is_valid = False
            receipt_file.invalid_reason = 'Not a PDF file'
            receipt_file.save()
            return Response({'message': 'Invalid file'}, status=400)

        receipt_file.is_valid = True
        receipt_file.invalid_reason = ''
        receipt_file.save()
        return Response({'message': 'File is valid'}, status=200)

class ReceiptProcessView(APIView):
    def post(self, request):
        receipt_id = request.data.get('id')
        try:
            receipt_file = ReceiptFile.objects.get(id=receipt_id, is_valid=True)
        except ReceiptFile.DoesNotExist:
            return Response({'error': 'Invalid or unvalidated receipt ID'}, status=404)

        # Convert and OCR
        import tempfile, re
        from pdf2image import convert_from_path
        from dateutil import parser as dateparser
        import pytesseract

        with tempfile.TemporaryDirectory() as path:
            images = convert_from_path(receipt_file.file.path, output_folder=path)

            full_text = ""
            for image in images:
                full_text += pytesseract.image_to_string(image) + "\n"

        # Parse details
        lines = full_text.splitlines()
        vendor = next((line.strip() for line in lines if line.strip()), None)

        date_regex = r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})'
        date_match = re.search(date_regex, full_text)
        date = None
        if date_match:
            try:
                date = dateparser.parse(date_match.group()).date()
            except:
                pass

        total = None
        amount_regex = r'(total|amount).*?(\d+\.\d{2})'
        for line in lines:
            match = re.search(amount_regex, line, re.IGNORECASE)
            if match:
                total = float(match.group(2))
                break

        # Save to DB
        Receipt.objects.create(
            receipt_file=receipt_file,
            raw_text=full_text,
            vendor_name=vendor,
            date=date,
            total_amount=total
        )
        receipt_file.is_processed = True
        receipt_file.save()

        return Response({'message': 'Receipt processed'}, status=200)


class ReceiptListView(ListAPIView):
    queryset = Receipt.objects.all().order_by('-processed_at')

    serializer_class = ReceiptSerializer


class ReceiptDetailView(RetrieveAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    lookup_field = 'pk'
