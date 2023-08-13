from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Place, Member, Meeting, Ticket, Booking
from .serializers import PlaceSerializer, MemberSerializer, MeetingSerializer, TicketSerializer, BookingSerializer


class GetPlacesView(APIView):
    def get(self, request):
        queryset = Place.objects.all()
        serializer_for_queryset = PlaceSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializer_for_queryset.data)


class GetMembersView(APIView):
    def get(self, request):
        queryset = Member.objects.all()
        serializer_for_queryset = MemberSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializer_for_queryset.data)


class GetMeetingsView(APIView):
    def get(self, request):
        queryset = Meeting.objects.all()
        serializer_for_queryset = MeetingSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializer_for_queryset.data)


class GetTicketsView(APIView):
    def get(self, request):
        queryset = Ticket.objects.all()
        serializer_for_queryset = TicketSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializer_for_queryset.data)


class GetBookingsView(APIView):
    def get(self, requests):
        queryset = Booking.objects.all()
        serializers_for_queryset = BookingSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializers_for_queryset.data)


