from django.urls import path
from components import views

urlpatterns = [
    path('',view=views.home)
]
