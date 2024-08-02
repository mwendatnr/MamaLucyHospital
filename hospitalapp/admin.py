from django.contrib import admin

from hospitalapp.models import patient,appointment,method

# Register your models here.

admin.site.register(patient)
admin.site.register(appointment)
admin.site.register(method)
