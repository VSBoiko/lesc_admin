from rest_framework import serializers
from .models import Place, Member, Meeting, Ticket, Booking


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class MeetingSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(source='place_id', read_only=True)

    class Meta:
        model = Meeting
        fields = ['name', 'date_time', 'place', 'can_be_booked', ]


class TicketSerializer(serializers.ModelSerializer):
    meeting = MeetingSerializer(source='meeting_id', read_only=True)

    class Meta:
        model = Ticket
        fields = ['meeting', 'price']


class BookingSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(source="ticket_id", read_only=True)
    member = MemberSerializer(source="member_id", read_only=True)

    class Meta:
        model = Booking
        fields = ['ticket', 'member', 'is_paid', 'date_time',]
