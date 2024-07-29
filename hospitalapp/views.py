from django.shortcuts import render,redirect
from hospitalapp.models import appointment,patient
from hospitalapp.forms import AppointmentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')

def Appointment(request):
    if request.method == 'POST':
        appointments= appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],

        )
        appointments.save()
        return redirect('/show')
    else:
        return render(request, 'appointment.html')

def show(request):
    myappointments = appointment.objects.all()
    return render(request, 'show.html', {'appointment':myappointments} )

def delete(request,id):
    appointment1 = appointment.objects.get(id=id)
    appointment1.delete()
    return redirect("/show")

def Patient(request):
    if request.method == 'POST':
        thepatients= patient(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            message = request.POST['message'],

        )
        thepatients.save()
        return redirect("/patientdetails")
    else:
        return render(request, 'patientdetails.html')

def pdetails(request):
    thepatients = patient.objects.all()
    return render(request,'patientdetails.html',{'patient':thepatients})
def edit(request,id):
    editappointment = appointment.objects.get(id=id)
    return render(request,'edit.html',{'appointment':editappointment})

def update(request,id):
    updateinfo = appointment.objects.get(id=id)
    form = AppointmentForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html')