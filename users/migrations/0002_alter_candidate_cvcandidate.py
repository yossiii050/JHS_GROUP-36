# Generated by Django 4.1.4 on 2023-01-07 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='cvcandidate',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.cvformmodel'),
        ),
    ]