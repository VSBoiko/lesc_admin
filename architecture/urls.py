from django.urls import path

from . import views

urlpatterns = [
    path('api/places/', views.GetPlacesView.as_view()),
    path('api/members/', views.GetMembersView.as_view()),
    path('api/meetings/', views.GetMeetingsView.as_view()),
    path('api/tickets/', views.GetTicketsView.as_view()),
    path('api/bookings/', views.GetBookingsView.as_view(),)
]
