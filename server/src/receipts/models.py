

from django.db import models

class ReceiptFile(models.Model):
    file = models.FileField(upload_to='receipts/')
    is_valid = models.BooleanField(default=False)
    invalid_reason = models.TextField(blank=True, null=True)
    processed_at = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Receipt(models.Model):
    receipt_file = models.OneToOneField(ReceiptFile, on_delete=models.CASCADE, related_name='receipt', null=True, blank=True)
    raw_text = models.TextField(null=True, blank=True)
    vendor_name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    processed_at = models.DateTimeField(auto_now_add=True)
