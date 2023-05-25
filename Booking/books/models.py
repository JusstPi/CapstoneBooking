from django.db import models
import random


def generate_referenceNo():
    length = 9

    while True:
        code = ''.join(random.choices('0123456789', k=length))
        if Booking.objects.filter(referenceNo=code).count() == 0:
            break
        return code
    
# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.username
    
class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,null=True)
    hasComputers = models.BooleanField(default=False, null=True)
    computers = models.IntegerField(null=True)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateField(null=True)
    startTime = models.TimeField(null=True)
    endTime = models.TimeField(null=True)
    purpose = models.CharField(max_length=50, null=True)
    #attendees = models.ManyToManyField(User)
    computers = models.IntegerField(null=True)
    referenceNo = models.CharField(max_length=20, unique=True, null=True)
    points = models.IntegerField(null=True)
    coins = models.IntegerField(null=True)
    status = models.CharField(max_length=10, null=True)
    duration = models.FloatField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)
    isUsed= models.BooleanField(default=False, null=True)
    #venue = (('Co-Wroking Space'), ('Conference A'), ('Conference B'))
    officeName = models.CharField(max_length=20, null=True)
    #type = models.CharField(max_length=1, choices=type_user)

    def __str__(self):
        return self.referenceNo
    
class BookingAttendee(models.Model):
    name = models.CharField(max_length=50, null=True)
    booking = models.ForeignKey(Booking, null=True, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, null=True, related_name='attendee', on_delete=models.CASCADE)
