from django.forms import ModelForm, DateInput
from .models import Student, LabRoom, RoomSlot
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form
class ReserveSlotForm(ModelForm):
    class Meta:
        model = Student
        fields =('name', 'email', 'major','slot','date','purpose')
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

class ReserveAnySlotForm(ModelForm):
    class Meta:
        model = Student
        fields =('name', 'email', 'major','slot','date','purpose')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']