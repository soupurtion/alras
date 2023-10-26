from django.db import models
from django.urls import reverse

# Create your models here.
class day(models.Model):
    Day = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
    )

class RoomSlot(models.Model):
    SLOTS = (
        ('slot-1', '09:00 - 12:00'),
        ('slot-2', '12:00 - 15:00'),
        ('slot-3', '15:00 - 18:00')
    )
    slot = models.CharField(max_length=200, choices= SLOTS)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('slot-detail', args=[str(self.id)])
    
class Student(models.Model):
    MAJOR = (
        ('PhD-CS', 'PhD in Computer Science'),
        ('PhD-Sec', 'PhD in Security'),
        ('MS-CS', 'MS in Computer Science'),
        ('MS-Sec', 'MS in Security'),
    )
    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)
    major = models.CharField(max_length=200, choices= MAJOR)
    slot = models.ForeignKey(RoomSlot, on_delete=models.CASCADE, unique=True, default = None)
    purpose = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

class LabRoom(models.Model):
    ROOMS = (
        ('101-A', 'Room 101-A'),
        ('102-A', 'Room 102-A'),
        ('103-B', 'Room 103-B'),
        ('104-B', 'Room 104-B'),
        ('105-C', 'Room 105-C'),
    )
    title = models.CharField(max_length=10,choices=ROOMS)
    slots = models.OneToOneField(RoomSlot, on_delete=models.CASCADE, unique=True, default=None)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('labroom-detail', args=[str(self.id)])