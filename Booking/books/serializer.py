from rest_framework import serializers
from .models import User, Venue, Booking, BookingAttendee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'password']

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['venue_id', 'name', 'hasComputers', 'computers']

class BookingAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingAttendee
        fields = ['name']

class BookingSerializer(serializers.ModelSerializer):
    attendees = BookingAttendeeSerializer(many=True)

    class Meta:
        model = Booking
        fields = "__all__"
