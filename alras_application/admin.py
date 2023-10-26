from django.contrib import admin
from .models import LabRoom, Student, RoomSlot

# Register your models here.
admin.site.register(LabRoom)
admin.site.register(RoomSlot)
admin.site.register(Student)