from django.contrib import admin
from .models import Member, Ticket, Place, Meeting, Booking
import copy


class MeetingAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "place_id", "date_time", "can_be_booked", ]
    list_display_links = ["id", "name", ]
    ordering = ['-date_time']
    actions = ['make_booked_true', 'make_booked_false', 'copy_meetings']

    @admin.action(description="Сделать выбранные Встречи доступными для бронирования")
    def make_booked_true(self, request, queryset):
        queryset.update(can_be_booked=True)

    @admin.action(description="Сделать выбранные Встречи не доступными для бронирования")
    def make_booked_false(self, request, queryset):
        queryset.update(can_be_booked=False)

    @admin.action(description="Копировать выбранные Встречи")
    def copy_meetings(self, request, queryset):
        for meeting in queryset:
            meeting_copy = copy.copy(meeting)
            meeting_copy.id = None
            meeting_copy.can_be_booked = False
            meeting_copy.save()


class TicketAdmin(admin.ModelAdmin):
    list_display = ["id", "meeting_id", "price", ]
    list_display_links = ["id", "meeting_id", ]
    order = ['-meeting_id']
    actions = ['copy_tickets', 'copy_tickets_four_times']

    @admin.action(description="Копировать выбранные Билеты")
    def copy_tickets(self, request, queryset):
        for ticket in queryset:
            ticket_copy = copy.copy(ticket)
            ticket_copy.id = None
            ticket_copy.save()

    @admin.action(description="Копировать выбранные Билеты 4 раза")
    def copy_tickets_four_times(self, request, queryset):
        for _ in range(0, 4):
            self.copy_tickets(request, queryset)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'address', 'link', 'description', ]
    list_display_links = ["id", "name", ]


class MemberAdmin(admin.ModelAdmin):
    list_display = ["id", 'tg_id', 'login', 'name', 'surname', ]
    list_display_links = ["id", "tg_id", ]


class BookingAdmin(admin.ModelAdmin):
    list_display = ["id", 'ticket_id', 'member_id', 'is_paid', 'date_time', ]
    list_display_links = ["id", "ticket_id", ]


admin.site.register(Member, MemberAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Booking, BookingAdmin)
