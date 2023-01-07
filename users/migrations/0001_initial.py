<<<<<<< HEAD
# Generated by Django 4.1.4 on 2023-01-06 00:53
=======
# Generated by Django 4.1.4 on 2023-01-03 16:12
>>>>>>> e590062d5ed2e64d838c14de65861287b204cf23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('candidate_id', models.CharField(max_length=200, unique=True)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CVFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.IntegerField(choices=[(1, 'Data science'), (2, 'Video game designer'), (3, 'Quality assurance engineer'), (4, 'CRM Project manager'), (5, 'Software intergration engineer'), (6, 'Data analyst'), (7, 'Full-Stack engineer')], default=1)),
                ('yearsexp', models.IntegerField(choices=[(1, '0-5'), (2, '5-10'), (3, '10-15'), (4, '15+')], default=1)),
                ('education', models.IntegerField(choices=[(1, 'B.A'), (2, 'B.Sc'), (3, 'Diploma'), (4, 'Practical engineer')], default=1)),
                ('GitUrl', models.URLField(max_length=25)),
                ('file', models.FileField(default='files/default.pdf', upload_to='files/')),
<<<<<<< HEAD
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('CompanyName', models.CharField(max_length=255)),
                ('employer_id', models.CharField(max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('employer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.employer')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.candidate')),
=======
>>>>>>> e590062d5ed2e64d838c14de65861287b204cf23
            ],
        ),
    ]
