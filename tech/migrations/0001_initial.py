<<<<<<< HEAD
# Generated by Django 4.1.4 on 2023-01-13 16:52
=======
<<<<<<< HEAD
# Generated by Django 4.1.4 on 2023-01-14 12:26
=======
# Generated by Django 4.1.4 on 2023-01-14 11:44
>>>>>>> a478816385a0e4201d600bd6dd6d225c02051692
>>>>>>> 7be1ea2057fde4b2f705ce0ac032ee7d317c2687

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
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Main claim')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('isopen', models.BooleanField(default=True)),
                ('Reply', models.TextField(blank=True, default=' ')),
                ('closed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='closed_by', to=settings.AUTH_USER_MODEL)),
                ('handler', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handler', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
