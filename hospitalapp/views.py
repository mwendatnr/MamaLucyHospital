import json

import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests.auth import HTTPBasicAuth

from hospitalapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from hospitalapp.models import appointment,patient,method
from hospitalapp.forms import AppointmentForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        if method.objects.filter(
                username=request.POST['username'],
                password=request.POST['password'],

        ).exists():
            return render(request,'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

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

def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)

def Register(request):
    if request.method == 'POST':
        registration= method(
            fullnamename = request.POST['fullname'],
            username = request.POST['username'],
            password = request.POST['password'],

        )
        registration.save()
        return redirect("/register")
    else:
        return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        mylogins= method(
            username = request.POST['username'],
            password = request.POST['password'],

        )
        mylogins.save()
        return redirect("/login")
    else:
        return render(request, 'login.html')



