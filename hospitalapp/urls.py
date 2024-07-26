
from django.contrib import admin
from django.urls import path

from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('inner/', views.inner,name='inner'),
    path('about/', views.about,name='about'),
    path('doctors/', views.doctors,name='doctors'),
    path('appointment/', views.Appointment,name='appointment'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),
    path('show2/', views.show2,name='show2'),
]
