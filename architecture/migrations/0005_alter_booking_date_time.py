# Generated by Django 4.2.4 on 2023-08-13 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('architecture', '0004_alter_booking_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
