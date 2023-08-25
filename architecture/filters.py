from django_filters import rest_framework as filters
from .models import Meeting, Booking


class MeetingFilter(filters.FilterSet):
    date_time_gte = filters.DateTimeFilter(field_name="date_time", lookup_expr='gte')
    date_time_lte = filters.DateTimeFilter(field_name="date_time", lookup_expr='lte')

    class Meta:
        model = Meeting
        fields = ['id', 'name', 'date_time', 'place_id', 'can_be_booked']


class BookingFilter(filters.FilterSet):
    date_time_gte = filters.DateTimeFilter(field_name='date_time', lookup_expr='gte')
    date_time_lte = filters.DateTimeFilter(field_name='date_time', lookup_expr='lte')

    class Meta:
        model = Booking
        fields = ['id', 'is_paid', 'member_id', 'date_time']
