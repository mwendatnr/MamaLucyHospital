from django import forms
from hospitalapp.models import appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['name','email','phone','date','department','doctor','message']