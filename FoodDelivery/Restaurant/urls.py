from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', homepage , name='landing'),
    path('navbar',displaynav,name = 'NAV'),
    path('login',Login, name='Login'),
    path('services',services,name="services"),
    path('afterlogin' ,afterlogin,name="afterlogin"),

    path('rr', restaurantregistration,name="rr"),
    path('reg',signup,name="reg"),
    path('contactus', contactus, name="contactus"),
    path('added',addedrestaurant,name="added"),
    path('delivery',Booking,name = 'Orderbooking')
]