from django import forms
from hospitalapp.models import appointment,method


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['name','email','phone','date','department','doctor','message']

class MethodForm(forms.ModelForm):
    class Meta:
        model = method
        fields = ['fullname','username','password']