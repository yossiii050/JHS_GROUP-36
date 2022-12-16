# Generated by Django 4.1.3 on 2022-12-16 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.IntegerField(choices=[(1, 'Data science'), (2, 'Video game designer'), (3, 'Quality assurance engineer'), (4, 'CRM Project manager'), (5, 'Software intergration engineer'), (6, 'Data analyst'), (7, 'Full-Stack engineer')], default=1)),
                ('yearsexp', models.IntegerField(choices=[(1, '0-5'), (2, '5-10'), (3, '10-15'), (4, '15+')], default=1)),
                ('education', models.IntegerField(choices=[(1, 'B.A'), (2, 'B.Sc'), (3, 'Diploma'), (4, 'Practical engineer')], default=1)),
                ('GitUrl', models.URLField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='upload',
            name='body',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='upload',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
    ]