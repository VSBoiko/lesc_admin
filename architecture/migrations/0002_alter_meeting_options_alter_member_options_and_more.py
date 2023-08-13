# Generated by Django 4.2.4 on 2023-08-13 12:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('architecture', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'verbose_name': 'Встречи'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Участники'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Места для встреч'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Билеты на встречи'},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='datetime',
        ),
        migrations.AddField(
            model_name='booking',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 13, 12, 41, 39, 860323)),
        ),
        migrations.AddField(
            model_name='meeting',
            name='can_be_booked',
            field=models.BooleanField(default=False, help_text='Встреча доступна для бронирования участниками', verbose_name='Можно бронировать'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Дата встречи', verbose_name='Дата'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='is_paid',
            field=models.BooleanField(default=False, help_text='Участник оплатил билет на встречу или нет', verbose_name='Статус оплаты'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='member_id',
            field=models.ForeignKey(help_text="Участник встречи из таблицы 'Участники'", on_delete=django.db.models.deletion.CASCADE, to='architecture.member', verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ticket_id',
            field=models.ForeignKey(help_text="Билет на встречу из таблицы 'Билеты на встречи'", on_delete=django.db.models.deletion.CASCADE, to='architecture.ticket', verbose_name='Билет на встречу'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='name',
            field=models.CharField(help_text='Название встречи', max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='place_id',
            field=models.ForeignKey(default=None, help_text="Место встречи из таблицы 'Места для встреч'", on_delete=django.db.models.deletion.SET_DEFAULT, to='architecture.place', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='member',
            name='login',
            field=models.CharField(help_text='Логин участника в Telegram', max_length=200, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(default=None, help_text='Имя участника в Telegram', max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='member',
            name='surname',
            field=models.CharField(default=None, help_text='Фамилия участника в Telegram', max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='member',
            name='tg_id',
            field=models.BigIntegerField(help_text='ID участника в Telegram', verbose_name='Telegram ID'),
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.TextField(help_text='Адрес места', max_length=500, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(help_text='Описание места', max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='link',
            field=models.URLField(help_text='Ссылку на место в Яндекс.Карты', max_length=500, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(help_text='Название места', max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='meeting_id',
            field=models.ForeignKey(help_text="Встреча из таблицы 'Встречи'", on_delete=django.db.models.deletion.CASCADE, to='architecture.meeting', verbose_name='Встреча'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.FloatField(help_text='Цена этого билета на выбранную встречу', verbose_name='Стоимость'),
        ),
    ]
