from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, LabRoom, RoomSlot
from django.views import generic
from .forms import ReserveSlotForm, ReserveAnySlotForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import Group

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
        context["students"] = Student.objects.filter(slot_id=a)
        return context

def reserveSlot(request, pk):
    slot_id = LabRoom.objects.filter(id=pk).values().all()[0]['slots_id']
    form = ReserveSlotForm()
    roomslot = RoomSlot.objects.get(id=slot_id)
    print(roomslot)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and slot_id
        student_data = request.POST.copy()
        student_data['slot_id'] = slot_id
        form = ReserveSlotForm(student_data)

        if form.is_valid():
            # Save the form without committing to the database
            student = form.save(commit=False)
            # Set the slot relationship
            student.slot = roomslot
            student.save()

            # Redirect back to the portfolio detail page
            return redirect('labroom-detail', slot_id)

    context = {'form': form,'roomslot':roomslot}
    return render(request, 'alras_application/reserve_slot.html', context)

def cancelSlot(request,pk):
    slot_id = LabRoom.objects.filter(id=pk).values().all()[0]['slots_id']
    roomslot = RoomSlot.objects.get(id=slot_id)
    student = Student.objects.get(slot_id=slot_id)
    if request.method == 'POST':
        student.delete()
        return redirect('labroom-detail', slot_id)
    
    return render(request,'alras_application/cancel_slot.html',{'pk':pk,'roomslot':roomslot})

def updateSlot(request, pk):
    slot_id = LabRoom.objects.filter(id=pk).values().all()[0]['slots_id']
    student = Student.objects.filter(slot_id=slot_id).values()[0]
    s_id = student['id']
    print(s_id)
    roomslot = RoomSlot.objects.get(id=slot_id)
    form = ReserveSlotForm(initial=student)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and slot_id
        student_data = request.POST.copy()
        student_data['slot_id'] = slot_id
        form = ReserveSlotForm(student_data)

        if form.is_valid():
            # Save the form without committing to the database
            student = form.save(commit=False)
            # Set the slot relationship
            student.slot = roomslot
            student.id = s_id
            student.save()

            # Redirect back to the portfolio detail page
            return redirect('labroom-detail', slot_id)

    context = {'form': form,'roomslot':roomslot,'pk':pk}
    return render(request, 'alras_application/update_slot.html', context)

'''
def reserveAnySlot(request):
    form = ReserveAnySlotForm()
    
    if request.method == 'POST':
        # Create a new dictionary with form data and slot_id
        student_data = request.POST.copy()
        form = ReserveSlotForm(student_data)

        if form.is_valid():
            # Save the form without committing to the database
            student = form.save(commit=False)
            # Set the slot relationship
           
            student.save()

            # Redirect back to the portfolio detail page
            return redirect('labroom')

    context = {'form': form}
    return render(request, 'alras_application/reserve_any_slot.html', context)

def cancelAnySlot(request):
    slot_id = LabRoom.objects.filter(id=pk).values().all()[0]['slots_id']
    roomslot = RoomSlot.objects.get(id=slot_id)
    student = Student.objects.get(slot_id=slot_id)
    if request.method == 'POST':
        student.delete()
        return redirect('labroom-detail', slot_id)
    
    return render(request,'alras_application/cancel_slot.html',{'pk':pk,'roomslot':roomslot})

def updateAnySlot(request):
    slot_id = LabRoom.objects.filter(id=pk).values().all()[0]['slots_id']
    student = Student.objects.filter(slot_id=slot_id).values()[0]
    s_id = student['id']
    print(s_id)
    roomslot = RoomSlot.objects.get(id=slot_id)
    form = ReserveSlotForm(initial=student)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and slot_id
        student_data = request.POST.copy()
        student_data['slot_id'] = slot_id
        form = ReserveSlotForm(student_data)

        if form.is_valid():
            # Save the form without committing to the database
            student = form.save(commit=False)
            # Set the slot relationship
            student.slot = roomslot
            student.id = s_id
            student.save()

            # Redirect back to the portfolio detail page
            return redirect('labroom-detail', slot_id)

    context = {'form': form,'roomslot':roomslot,'pk':pk}
    return render(request, 'alras_application/update_slot.html', context)
'''

def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='student')
            user.groups.add(group)
            student = Student.objects.create(user=user)
            student.save()

            messages.success(request,'Account was created for '+username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)

