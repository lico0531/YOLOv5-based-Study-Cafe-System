from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from main.db import collection  # MongoDB 컬렉션 가져오기

def index(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            
            # MongoDB에 유저 데이터 삽입
            user_data = {"username": username, "password": password, "email": email}
            collection.insert_one(user_data)
            
            return redirect('index')

        elif 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            
            # MongoDB에서 유저 데이터 조회
            user = collection.find_one({"username": username, "password": password})
            if user:
                # Django 세션에 로그인 상태 저장
                request.session['username'] = username
                return redirect('seat')
            else:
                return render(request, 'index.html', {'error': 'Invalid credentials'})

    return render(request, 'index.html')

def seat(request):
    if 'username' not in request.session:
        return redirect('index')
    return render(request, 'seat.html')