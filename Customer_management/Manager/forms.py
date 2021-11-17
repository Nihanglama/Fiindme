from django.db import models
from .models import Customer, Order, Product
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class Signup(UserCreationForm):
          class Meta:
                    model=User
                    fields=['username','email','password1','password2']

class Customer_form(ModelForm):
          class Meta:
                    model=Customer
                    fields='__all__'
                    exclude=['user']

class Product_form(ModelForm):
          class Meta:
                    model=Product    
                    fields='__all__'
                    

class Place_order(ModelForm):
          class Meta:
                    model=Order
                    fields=['phone','address','quentity']
                    

