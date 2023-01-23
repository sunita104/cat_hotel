from django.db import models
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    number_room = models.CharField(max_length=10, primary_key=True)
    description = models.TextField(max_length=300,null=True)

    def __str__(self):
        return self.number_room

class Booking(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    description = models.TextField(max_length=200,null=True)
    start_date = models.DateField(auto_now_add=True,null=True)
    start_time = models.TimeField(auto_now_add=True,null=True)
    end_date = models.DateField(auto_now_add=True,null=True)
    end_time = models.TimeField(auto_now_add=True,null=True)
    cat = models.TextField(max_length=200,null=True)
    phone_number = models.TextField(max_length=200,null=True)

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name