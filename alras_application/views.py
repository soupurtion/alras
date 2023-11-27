from django.shortcuts import render, redirect
from .models import Student, LabRoom
from django.views import generic
from .forms import ReserveSlotForm, CreateUserForm, StudentForm
from django.contrib import messages
from django.contrib.auth.models import Group
from datetime import datetime, timedelta
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users





# Create your views here.
def index(request):
    today = datetime.now().date()
    student_active_today = Student.objects.filter(date=today)
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
        #today = datetime.now().date()
        today = self.kwargs['date']
        #print(self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        #print(self.objects.values().all())
        #a = LabRoom.objects.filter(id=self.kwargs['pk']).values().all()[0]['slot_id']
        #print(a)
        #context["roomslot"] = RoomSlot.objects.filter(id=a)
        context["students"] = Student.objects.filter(slot_id=self.kwargs['pk'],date=today)
        context['date'] = today
        #print(context["students"])
        return context

@login_required(login_url='login')
@allowed_users(allowed_roles=['student_role'])
def reserveSlot(request, pk, date):
    #print(pk)
    #slot_id = LabRoom.objects.filter(id=pk).values().all()[0]['slot_id']
    #print(slot_id)
    form = ReserveSlotForm()
    #roomslot = RoomSlot.objects.get(id=slot_id)
    #print(roomslot)
    #print(LabRoom.objects.filter(id=pk))
    labroom = LabRoom.objects.get(id=pk)
    print(request.user.id)
    if request.method == 'POST':
        # Create a new dictionary with form data and slot_id
        student_data = request.POST.copy()
        student_data['slot_id'] = pk
        student_data['date'] = date
        student_data['user_id'] = request.user.id
        print(student_data)

        form = ReserveSlotForm(student_data)
        if form.is_valid():
            # Save the form without committing to the database
            student = form.save(commit=False)
            # Set the slot relationship
            student.slot_id = pk
            student.date = date
            student.user_id = request.user.id
            student.save()

            # Redirect back to the portfolio detail page
            return redirect('labroom-detail', pk, date)

    context = {'form': form,'labroom':labroom,'date':date}
    return render(request, 'alras_application/reserve_slot.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['student_role'])
def cancelSlot(request,pk,date):

    labroom = LabRoom.objects.get(id=pk)
    student = Student.objects.get(slot_id=pk,date=date)
   
    date  = date
    if request.method == 'POST':
        student.delete()
        return redirect('labroom-detail', pk, date)
    return render(request,'alras_application/cancel_slot.html',{'pk':pk,'labroom':labroom,'date':date})




@login_required(login_url='login')
@allowed_users(allowed_roles=['student_role'])
def updateSlot(request, pk, date):
    
    student = Student.objects.filter(slot_id=pk,date=date).values()[0]
    s_id = student['id']
    print(student)
    
    form = ReserveSlotForm(initial=student)
    labroom = LabRoom.objects.get(id=pk)
    date = date
    if request.method == 'POST':
        # Create a new dictionary with form data and slot_id
        student_data = request.POST.copy()
        student_data['slot_id'] = pk
        student_data['date'] = date
        form = ReserveSlotForm(student_data)

        if form.is_valid():
            # Save the form without committing to the database
            student = form.save(commit=False)
            # Set the slot relationship
            student.slot_id = pk
            student.id = s_id
            student.date = date
            student.save()

            # Redirect back to the portfolio detail page
            return redirect('labroom-detail', pk, date)

    context = {'form': form,'labroom':labroom,'pk':pk,'date':date}
    return render(request, 'alras_application/update_slot.html', context)



def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='student_role')
            user.groups.add(group)
            #student = Student.objects.create(user=user)
            #student.save()

            messages.success(request,'Account was created for '+username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)





def labroom_list(request):
    labrooms = LabRoom.objects.all()
    

    today = datetime.now().date()
    dates = []
   
    labroom_list = [labroom for labroom in labrooms]
    table_data = []

    for i in range(7):
        dates.append(today)
        today = datetime.now().date() + timedelta(days=i+1)
    view_urls_datewise = []

    
    for labroom in labrooms:
        today = datetime.now().date()
        temp = []
        for i in range(7):

            vur_url = {}

            
            vur_url["view"] = reverse('labroom-detail', args=[labroom.pk, str(today)])

            student = Student.objects.filter(slot_id = labroom.id, date=today).values().all()
            if student.exists():
                vur_url["update"] = (reverse('update_slot', args=[labroom.pk, str(today)]))
            else:
                vur_url["reserve"] = (reverse('reserve_slot', args=[labroom.pk, str(today)]))

            temp.append(vur_url)
            #temp.append(reverse('labroom-detail', args=[labroom.pk, str(today)]))
            today = datetime.now().date() + timedelta(days=i+1)
        
        view_urls_datewise.append(temp)
        table_data.append({'labroom':labroom,'urls':temp})


    context = {'views_url': view_urls_datewise,'dates':dates,'labrooms':labroom_list,'data':table_data}
    return render(request, 'alras_application/labroom_list.html', context)


def userPage(request):
    user_id = request.user.id
    student_slots = Student.objects.filter(user_id=user_id)
    print(student_slots)
    student_slots.filter(name='').delete()

    if student_slots:
        i = 1
    else:
        i = 0
    
    return render(request,'alras_application/user.html',{'student_slots':student_slots,'i':i})


