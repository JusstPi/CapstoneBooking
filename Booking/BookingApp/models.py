from django.db import models
import random


def generate_referenceNo():
    length = 9

    while True:
        code = ''.join(random.choices(k=length))
        if Booking.objects.filter(referenceNo=code).count() == 0:
            break
        return code
    
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
    createdAt = models.DateField(auto_now_add=True)
    date = models.DateField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    purpose = models.CharField(max_length=50)
    #attendees = models.ManyToManyField(User)
    computers = models.IntegerField()
    referenceNo = models.CharField(max_length=20, unique=True)
    points = models.IntegerField()
    coins = models.IntegerField()
    status = models.CharField(max_length=5)
    duration = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE)
    isUsed= models.BooleanField()
    #type = models.CharField(max_length=1, choices=type_user)

    def __str__(self):
        return self.referenceNo