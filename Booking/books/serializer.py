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

class BookingAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingAttendee
        fields=('__all__')

class BookingSerializer(serializers.ModelSerializer):
    attendees = BookingAttendeeSerializer(many=True)

    class Meta:
        model = Booking
        fields = "__all__"

    def create(self, validated_data):
        attendees=validated_data.pop('attendees')
        booking=Booking(**validated_data)        
        booking.save()
        serializer= BookingAttendeeSerializer(data=attendees,many=True)
        if serializer.is_valid(raise_exception=True):
            attendees=serializer.save(booking=booking)
        return booking
