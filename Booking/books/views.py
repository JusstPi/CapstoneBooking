from django.shortcuts import render
from rest_framework import generics
from .models import CalendarEvent,User, Venue, Booking, BookingAttendee
from .serializers import UserSerializer, VenueSerializer, BookingSerializer


class Useriew(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VenueView(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

