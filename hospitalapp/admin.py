from django.contrib import admin

from hospitalapp.models import patient,appointment

# Register your models here.

admin.site.register(patient)
admin.site.register(appointment)
