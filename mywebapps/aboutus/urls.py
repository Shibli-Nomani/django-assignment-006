from django.urls import path
from . import views

urlpatterns = [
    path('', views.About_Us),
    path('profiles/', views.Profiles),
]