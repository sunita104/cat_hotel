from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(requset):
    return render(requset, 'cat_hotel/home.html')

def about(requset):
    return render(requset, 'cat_hotel/about.html')

def profile(requset):
    return render(requset, 'cat_hotel/profile.html')

def login_user(requset):
    return render(requset, 'cat_hotel/login_user.html')

def cat_hotels(requset):
    return render(requset,'cat_hotel/cat_hotels.html')

def cat_hotel(requset):
    return render(requset,'cat_hotel/cat_hotel.html')

def completed(requset):
    return render(requset,'cat_hotel/completed.html')

def edit_completed(requset):
    return render(requset,'cat_hotel/edit_completed.html')