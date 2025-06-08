from django.db import models

class Receipt(models.Model):
    file = models.FileField(upload_to='receipts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    vendor_name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    total_amount = models.CharField(max_length=100, blank=True, null=True)
    raw_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Receipt {self.id} - {self.vendor_name or 'Unknown'}"
