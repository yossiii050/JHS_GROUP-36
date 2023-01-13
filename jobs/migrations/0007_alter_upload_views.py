# Generated by Django 4.1.4 on 2023-01-11 10:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0006_alter_upload_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='views',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
