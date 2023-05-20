from django.db import models
import random


def generate_referenceNo():
    length = 9

    while True:
        code = ''.join(random.choices(k=length))
        if Booking.objects.filter(referenceNo=code).count() == 0:
            break
        return code

OFFICENAMES = (
	('Conference Room A', 'Conference Room A'),
	('Conference Room B', 'Conference Room B'),
	('Coworking Space', 'Coworking Space'),
)
    
# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    hasComputers = models.BooleanField(default=False, null=False)
    computers = models.IntegerField()

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    purpose = models.CharField(max_length=50)
    #attendees = models.ManyToManyField(User)
    computers = models.IntegerField()
    referenceNo = models.CharField(max_length=20, unique=True)
    points = models.IntegerField()
    coins = models.IntegerField()
    status = models.CharField(max_length=10)
    duration = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE)
    isUsed= models.BooleanField(default=False)
    #officeNames = (('Co-Wroking Space'), ('Conference A'), ('Conference B'))
    officeName = models.CharField(max_length=20, choices=OFFICENAMES, null=False, default='Coworking Space')
    #type = models.CharField(max_length=1, choices=type_user)

    def __str__(self):
        return self.referenceNo
    
class BookingAttendee(models.Model):
    booking = models.ForeignKey(Booking, null=True, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, null=True, related_name='attendee', on_delete=models.CASCADE)