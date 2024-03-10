from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import restaurant

from .forms import SubscribeForm
from .models import restaurant, Booking


# Create your views here.
def displaynav(request):
    return render(request,'navbar.html')

def homepage(request):
    return render(request,'homepage.html')
def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.info(request, 'Username (or) Password is incorrect')

    context = {}
    return render(request, 'Login.html', context)


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('landing')
    messages.success(request, f'{request.user} has been succesfully logged out.')
    logout(request)
    return redirect('Login')


def services(request):
    return render(request,'services.html')



def afterlogin(request):
    return render(request,'afterlogin.html')


def restaurantregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        rname = request.POST["restaurant_name"]
        address = request.POST["address"]
        email = request.POST["email"]
        password = request.POST["password"]
        restaurant_id = request.POST["restaurant_id"]
        res = restaurant(name=name,restaurant_name=rname, address=address, Email_address=email, Password=password, restaurant_id=restaurant_id)
        res.save()
        return redirect('added')

    return render(request, 'registerrestaurant.html')
def delivery_booking(request):

    if request.method == 'POST':
        username = request.POST['user_name']
        fromadd = request.POST['From_address']
        toadd = request.POST['To_address']
        orderfood = request.POST['Order_food']
        orderrest = request.POST['Ordered_restaurant']
        book = Booking(user_name = username,From_address = fromadd , To_address = toadd, Order_food = orderfood,Ordered_restaurant =orderrest)
        book.save()
        return redirect('Orderbooking')
    return render(request,'delivery.html')
def signup(request):
     return render(request,'Signup.html')

def contactus(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'issues'
            prob = request.POST.get('problem')
            message = prob
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
                      message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'mail sent successfully')
            return redirect('contactus')
    return render(request, 'contactus.html',{'form':form})


def addedrestaurant(request):
    restaurants = restaurant.objects.all()
    return render (request,'addedresturant.html',{'restaurants': restaurants})


