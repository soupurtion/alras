from django.forms import ModelForm
from .models import Student, LabRoom, RoomSlot
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form
class ReserveSlotForm(ModelForm):
    class Meta:
        model = Student
        fields =('name', 'email', 'major','purpose')

class ReserveAnySlotForm(ModelForm):
    class Meta:
        model = Student
        fields =('name', 'email', 'major','slot','purpose')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']