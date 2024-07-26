from django.shortcuts import render,redirect
from hospitalapp.models import appointment

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

def show2(request):
    myappointments = appointment.objects.all()
    return render(request,'show2.html')