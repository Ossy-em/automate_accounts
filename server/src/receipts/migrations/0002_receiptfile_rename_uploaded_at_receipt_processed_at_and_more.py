# Generated by Django 5.2.2 on 2025-06-09 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='receipts/')),
                ('is_valid', models.BooleanField(default=False)),
                ('invalid_reason', models.TextField(blank=True, null=True)),
                ('processed_at', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='uploaded_at',
            new_name='processed_at',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='file',
        ),
        migrations.AlterField(
            model_name='receipt',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='receipt_file',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receipt', to='receipts.receiptfile'),
        ),
    ]
