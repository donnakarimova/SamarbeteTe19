from django.shortcuts import render

# Create your views here.
def mainsite(request):
    return render(request, 'mainsite.html')
    #Person 4 här behövs kod skapas för att visa mainsidan från templates.