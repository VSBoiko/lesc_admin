from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Place, Member, Meeting, Ticket, Booking
from .serializers import PlaceSerializerBase, MemberSerializer, MeetingSerializer, TicketSerializer, BookingSerializer


class GetPlacesView(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializerBase


class GetMembersView(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class GetMeetingsView(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class GetTicketsView(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class GetBookingsView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
