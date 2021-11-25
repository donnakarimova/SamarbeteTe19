
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Person 1, Använd include för att kopp tilla mainsite.urls, register.urls och shop.urls
    path('',)),
    path('register/', ),
    path('shop/', ),
]
