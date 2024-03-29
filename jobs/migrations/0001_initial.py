# Generated by Django 4.1.4 on 2023-01-14 19:28

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, null=True)),
                ('subTitle', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.IntegerField(choices=[(1, 'Data science'), (2, 'Video game designer'), (3, 'Quality assurance engineer'), (4, 'CRM Project manager'), (5, 'Software intergration engineer'), (6, 'Data analyst'), (7, 'Full-Stack engineer')], default=1)),
                ('salaryRange', models.IntegerField(choices=[(1, '0-10000'), (2, '10000-15000'), (3, '15000-30000'), (4, '30000+')], default=1)),
                ('yearsexp', models.IntegerField(choices=[(1, '0-5'), (2, '5-10'), (3, '10-15'), (4, '15+')], default=1)),
                ('education', models.IntegerField(choices=[(1, 'B.A'), (2, 'B.Sc'), (3, 'Diploma'), (4, 'Practical engineer')], default=1)),
                ('time', models.IntegerField(choices=[(1, 'full time'), (2, 'part time'), (3, 'shifts')], default=1)),
                ('hybrid', models.BooleanField(default=True)),
                ('priority', models.IntegerField(choices=[(1, 'high priority'), (2, 'mid priority'), (3, 'low priority')], default=1)),
                ('location', models.IntegerField(choices=[(1, 'Jerusalem'), (2, 'Tel Aviv'), (3, 'Haifa'), (4, 'Rishon Le Zion'), (5, 'Beersheba')], default=1)),
                ('viewsCounter', models.IntegerField(default=0)),
                ('availableAmount', models.DecimalField(decimal_places=0, default=Decimal('5'), max_digits=2)),
                ('notification', models.DecimalField(decimal_places=0, default=Decimal('5'), max_digits=3)),
                ('notification_count', models.IntegerField(default=0)),
                ('applycandiadteuser', models.ManyToManyField(blank=True, null=True, to='users.candidate')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='users.employer')),
            ],
        ),
    ]
