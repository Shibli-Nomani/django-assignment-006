from django.urls import path
from . import views

urlpatterns = [
    path('flightdetails', views.Flight_Details),
   
]