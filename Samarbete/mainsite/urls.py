from django.contrib import admin
from django.urls import path,include
from . import views
#((Person 1) här behövs läggas till en koppling till view

urlpatterns = [
    # Person 4, här behövs kopplas till view-funktionen mainsite
    path('',    views.mainsite  , name="mainsite"),
]