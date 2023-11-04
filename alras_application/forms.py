from django.forms import ModelForm
from .models import Student, LabRoom, RoomSlot


#create class for project form
class ReserveSlotForm(ModelForm):
    class Meta:
        model = Student
        fields =('name', 'email', 'major','purpose')

class ReserveAnySlotForm(ModelForm):
    class Meta:
        model = Student
        fields =('name', 'email', 'major','slot','purpose')

