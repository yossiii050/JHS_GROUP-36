# Generated by Django 4.1.4 on 2023-01-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CVForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.IntegerField(choices=[(1, 'Data science'), (2, 'Video game designer'), (3, 'Quality assurance engineer'), (4, 'CRM Project manager'), (5, 'Software intergration engineer'), (6, 'Data analyst'), (7, 'Full-Stack engineer')], default=1)),
                ('yearsexp', models.IntegerField(choices=[(1, '0-5'), (2, '5-10'), (3, '10-15'), (4, '15+')], default=1)),
                ('education', models.IntegerField(choices=[(1, 'B.A'), (2, 'B.Sc'), (3, 'Diploma'), (4, 'Practical engineer')], default=1)),
                ('GitUrl', models.URLField(max_length=25)),
            ],
        ),
    ]
