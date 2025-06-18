from django.urls import path
from .views import (
    ReceiptUploadView,
    ReceiptValidationView,
    ReceiptProcessView,
    ReceiptListView,
    ReceiptDetailView,
)

urlpatterns = [
    path('upload/', ReceiptUploadView.as_view(), name='upload'),
    path('validate/', ReceiptValidationView.as_view(), name='validate'),
    path('process/', ReceiptProcessView.as_view(), name='process'),
    path('receipts/', ReceiptListView.as_view(), name='receipt-list'),
    path('receipts/<int:pk>/', ReceiptDetailView.as_view(), name='receipt-detail'),
]

