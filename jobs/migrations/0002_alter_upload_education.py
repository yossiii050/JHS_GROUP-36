# Generated by Django 4.1.4 on 2023-01-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='education',
            field=models.IntegerField(choices=[(1, 'B.A'), (2, 'B.Sc'), (3, 'Diploma'), (4, 'Practical engineer')], default=1),
        ),
    ]