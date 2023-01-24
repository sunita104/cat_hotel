from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

all_room = [
    {'room': 101, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 102, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 103, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 104, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 105, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 106, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 107, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 108, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 109, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 110, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 111, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 112, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 113, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 114, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
    {'room': 115, 'description': '(ขนาดห้อง 1.7 x 1.4 x 2.6 หรือ 2.0 x 1.2 x 2.6 ม.) 300 บาท / วัน / น้องแมว 1-3 ตัว'},
]


def home(requset):
    return render(requset, 'cat_hotel/home.html')

def about(requset):
    return render(requset, 'cat_hotel/about.html')

def profile(requset):
    return render(requset, 'cat_hotel/profile.html')

def login_user(requset):
    return render(requset, 'cat_hotel/login_user.html')

def cat_hotels(requset):
    context = {'cat_hotels': all_room}
    return render(requset,'cat_hotel/cat_hotels.html', context)

def cat_hotel(requset, room_id):
    one_room =None
    try:
        one_room = [f for f in all_room if f['room']==room_id][0]
    except IndexError:
        print('ไม่พบข้อมูล')
    context = { 'cat_hotel':one_room}
    return render(requset,'cat_hotel/cat_hotel.html', context)

def completed(requset):
    return render(requset,'cat_hotel/completed.html')

def edit_completed(requset):
    return render(requset,'cat_hotel/edit_completed.html')