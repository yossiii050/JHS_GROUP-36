# Generated by Django 4.1.4 on 2023-01-05 16:48

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_upload_location_upload_owner_upload_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='availableAmount',
            field=models.DecimalField(decimal_places=0, default=Decimal('1'), max_digits=3),
        ),
    ]
