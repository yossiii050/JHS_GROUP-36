# Generated by Django 4.1.4 on 2023-01-07 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_candidate_cvcandidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='cvcandidate',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.cvformmodel'),
        ),
    ]