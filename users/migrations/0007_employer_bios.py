# Generated by Django 4.1.4 on 2023-01-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_candidate_bios'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='bios',
            field=models.TextField(blank=True, default='write you bio here...'),
        ),
    ]