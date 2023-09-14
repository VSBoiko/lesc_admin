from django.db import models
from django.utils import timezone


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название", help_text="Название места")
    address = models.TextField(max_length=500, verbose_name="Адрес", help_text="Адрес места")
    link = models.URLField(max_length=500, verbose_name="Ссылка", help_text="Ссылку на место в Яндекс.Карты")
    description = models.TextField(max_length=500, default="", null=True, blank=True, verbose_name="Описание",
                                   help_text="Описание места")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Место для встреч'
        verbose_name_plural = "Места для встреч"


class Meeting(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название", help_text="Название встречи")
    date_time = models.DateTimeField(verbose_name="Дата", help_text="Дата встречи")
    place_id = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, verbose_name="Место",
                                 help_text="Место встречи из таблицы 'Места для встреч'")
    can_be_booked = models.BooleanField(default=False, verbose_name="Можно бронировать",
                                        help_text="Встреча доступна для бронирования участниками")

    def __str__(self):
        return f"{self.place_id} - {self.date_time.strftime('%d %B %Y %H:%M')}"

    class Meta:
        verbose_name = "Встреча"
        verbose_name_plural = "Встречи"


class Ticket(models.Model):
    meeting_id = models.ForeignKey(Meeting, on_delete=models.SET_NULL, null=True, verbose_name="Встреча",
                                   help_text="Встреча из таблицы 'Встречи'", related_name='tickets')
    price = models.FloatField(verbose_name="Стоимость", help_text="Цена этого билета на выбранную встречу")

    def __str__(self):
        return f"{self.meeting_id} {self.price}"

    class Meta:
        verbose_name = "Билет на встречу"
        verbose_name_plural = "Билеты на встречи"


class Member(models.Model):
    tg_id = models.BigIntegerField(verbose_name="Telegram ID", help_text="ID участника в Telegram")
    login = models.CharField(max_length=200, verbose_name="Логин", default=None, null=True, blank=True,
                             help_text="Логин участника в Telegram")
    name = models.CharField(max_length=200, default=None, null=True, blank=True, verbose_name="Имя",
                            help_text="Имя участника в Telegram")
    surname = models.CharField(max_length=200, default=None, null=True, blank=True, verbose_name="Фамилия",
                               help_text="Фамилия участника в Telegram")

    def __str__(self):
        title_list = [
            self.name,
            self.surname,
            f"[{self.login}]",
        ]
        title = " ".join(filter(None, title_list))
        return title

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


class Booking(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, verbose_name="Билет на встречу",
                                  help_text="Билет на встречу из таблицы 'Билеты на встречи'", related_name='booking')
    member_id = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, verbose_name="Участник",
                                  help_text="Участник встречи из таблицы 'Участники'", related_name='bookings')
    is_paid = models.BooleanField(default=False, verbose_name="Статус оплаты",
                                  help_text="Мы подтвердили оплату билета на встречу или нет")
    user_confirm_paid = models.BooleanField(default=False, verbose_name="Участник подтвердил оплату",
                                  help_text="Участник подтвердил оплату билета на встречу или нет")
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    def __str__(self):
        is_paid = "Оплачено" if self.is_paid else "Не оплачено"
        return f"{self.member_id}: {self.member_id} - {is_paid}"
