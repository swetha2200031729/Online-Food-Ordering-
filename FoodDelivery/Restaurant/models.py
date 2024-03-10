from django.db import models


class restaurant(models.Model):
    name = models.CharField(unique=True, max_length=50, default='john' )
    restaurant_name = models.CharField(max_length=40, default='name')
    restaurant_id = models.IntegerField(default='3')
    address = models.TextField(default='vjd')
    Email_address = models.CharField(default='email')
    Password = models.CharField(default='password')

class Booking(models.Model):
    user_name = models.CharField(max_length = 50,default = 'jambu')
    From_address = models.TextField(max_length=100)
    To_address = models.TextField(max_length = 100)
    Ordered_restaurant = models.CharField(max_length=30)
    Ordered_food = models.CharField(max_length=40)

