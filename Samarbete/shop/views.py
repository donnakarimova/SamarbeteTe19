from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request, 'shop.html')
    #Person 5 här ska en länk till template filen shop visas.