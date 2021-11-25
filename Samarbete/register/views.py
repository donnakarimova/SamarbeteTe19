from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request,'register.html')
    #Person 3 här behövs kod skapas för att visa en register sida från templates. Kolla förra uppgiften
    #inspiration