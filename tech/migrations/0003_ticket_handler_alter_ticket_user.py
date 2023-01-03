# Generated by Django 4.1.4 on 2023-01-03 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tech', '0002_ticket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='handler',
            field=models.ForeignKey(default=None,null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handler', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(default=None,null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
