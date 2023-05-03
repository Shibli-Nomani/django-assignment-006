from django.urls import path
from . import views

urlpatterns = [
    path('attraction', views.Attractions),
    path('blogs', views.Blogs),
]