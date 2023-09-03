from rest_framework import serializers
from .models import Place, Member, Meeting, Ticket, Booking


class PlaceSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class BookingSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class MemberSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class TicketSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class MeetingSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    member = MemberSerializerBase(source='member_id', read_only=True)
    ticket = TicketSerializerBase(source='ticket_id', read_only=True)

    class Meta:
        model = Booking
        fields = ["pk", 'is_paid', 'date_time', 'member', 'ticket']


class MemberSerializer(serializers.ModelSerializer):
    bookings = BookingSerializerBase(many=True)

    class Meta:
        model = Member
        fields = ["pk", "tg_id", "login", "name", "surname", "bookings", ]


class TicketSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ['pk', 'price', 'booking', ]


class MeetingSerializer(serializers.ModelSerializer):
    place = PlaceSerializerBase(source='place_id', read_only=True)
    tickets = TicketSerializer(many=True)

    class Meta:
        model = Meeting
        fields = ["pk", 'name', 'date_time', 'place', 'can_be_booked', 'tickets', ]
