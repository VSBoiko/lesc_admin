from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Place, Member, Meeting, Ticket, Booking
from .serializers import PlaceSerializerBase, MemberSerializer, MeetingSerializer, TicketSerializer, BookingSerializer
from .filters import MeetingFilter, BookingFilter


class GetPlacesView(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializerBase
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['id', 'name', 'address', 'link', 'description']

    def create(self, request, *args, **kwargs):
        new_obj = Place.objects.create(**request.data)
        new_obj.save()
        serializer = self.serializer_class(new_obj)
        return Response(serializer.data)


class GetMembersView(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['id', 'tg_id', 'login', 'name', 'surname']

    def create(self, request, *args, **kwargs):
        new_obj = Member.objects.create(**request.data)
        new_obj.save()
        serializer = self.serializer_class(new_obj)
        return Response(serializer.data)


class GetMeetingsView(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MeetingFilter

    def create(self, request, *args, **kwargs):
        new_obj = Meeting.objects.create(**request.data)
        new_obj.save()
        serializer = self.serializer_class(new_obj)
        return Response(serializer.data)


class GetTicketsView(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['id', ]

    def create(self, request, *args, **kwargs):
        new_obj = Ticket.objects.create(**request.data)
        new_obj.save()
        serializer = self.serializer_class(new_obj)
        return Response(serializer.data)


class GetBookingsView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = BookingFilter

    def create(self, request, *args, **kwargs):
        ticket = get_object_or_404(Ticket, pk=request.data.get("ticket_id"))
        member = get_object_or_404(Member, pk=request.data.get("member_id"))
        params = {
            "date_time": request.data.get("date_time"),
            "is_paid": request.data.get("is_paid"),
            "ticket_id": ticket,
            "member_id": member,
        }
        new_obj = Booking.objects.create(**params)
        new_obj.save()
        serializer = self.serializer_class(new_obj)
        return Response(serializer.data)

    def remove(self, request, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=request.data.get("pk"))
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
