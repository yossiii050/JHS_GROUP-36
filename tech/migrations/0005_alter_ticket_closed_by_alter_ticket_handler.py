# Generated by Django 4.1.4 on 2023-01-07 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tech', '0004_alter_ticket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='closed_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='closed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='handler',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handler', to=settings.AUTH_USER_MODEL),
        ),
    ]