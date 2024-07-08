from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from .models import Seat, User
import json

def index(request):
    return render(request, 'index.html')

def seat(request):
    return render(request, 'seat.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'success': True})
        except:
            return JsonResponse({'success': False, 'message': 'User already exists'})

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return JsonResponse({'success': True})

def check_login_status(request):
    if request.user.is_authenticated:
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@csrf_exempt
def select_seat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        seat_number = data['seat']
        # Logic to select a seat
        return JsonResponse({'success': True})

@csrf_exempt
def deselect_seat(request):
    if request.method == 'POST':
        # Logic to deselect a seat
        return JsonResponse({'success': True})

def fetch_seat_info(request):
    if request.method == 'GET':
        seats = Seat.objects.all()
        seat_list = [{'seat': seat.number, 'status': seat.status} for seat in seats]
        return JsonResponse({'success': True, 'seats': seat_list})
