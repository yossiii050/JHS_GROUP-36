# Generated by Django 4.1.4 on 2022-12-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
