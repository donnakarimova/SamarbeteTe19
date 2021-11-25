from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import response
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate

# Create your views here.
def register(response):
    #Person 8, här behövs kod för att skicka ett response med en form skapas (Ta hjälp av tidigare uppgiften)
