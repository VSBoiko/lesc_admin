# Generated by Django 4.2.4 on 2023-08-13 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architecture', '0002_alter_meeting_options_alter_member_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 13, 12, 43, 4, 707344)),
        ),
    ]
