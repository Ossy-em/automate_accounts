from rest_framework import serializers
from .models import Receipt, ReceiptFile

class ReceiptFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptFile
        fields = '__all__'

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = [
            'id',
            'receipt_file',
            'vendor_name',
            'date',
            'total_amount',
            'raw_text',
            'processed_at',
        ]
