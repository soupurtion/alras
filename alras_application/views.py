from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, LabRoom, RoomSlot
from django.views import generic

# Create your views here.
def index(request):
    student_active_today = Student.objects.all()
    return render( request, 'alras_application/index.html',{'student_active_today':student_active_today})


class StudentDetailView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class LabRoomListView(generic.ListView):
    model = LabRoom

class LabRoomDetailView(generic.DetailView):
    model = LabRoom
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(self.objects.values().all())
        a = LabRoom.objects.filter(id=self.kwargs['pk']).values().all()[0]['slots_id']
        context["roomslot"] = RoomSlot.objects.filter(id=a)
        context["students"] = Student.objects.filter(id=a)
        print(context["students"].values().all())
        return context