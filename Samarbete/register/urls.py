from django.contrib import admin
from django.urls import path
from . import views
#((Person 2) här behövs läggas till en koppling till view

urlpatterns = [
    #((Person 2) här behövs läggas till en koppling till view-funktionen register)
    path('',  views.register, name="register"),

]