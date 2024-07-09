from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from main.db import collection  # MongoDB 컬렉션 가져오기

def index(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            
            # Check if user with the same username already exists
            existing_user = collection.find_one({"username": username})
            if existing_user:
                return render(request, 'index.html', {'error': '이미 있는 id입니다.'})
            
            # MongoDB에 유저 데이터 삽입
            user_data = {"username": username, "password": password, "seat": None}  # 좌석 번호를 null로 설정
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
    
    if request.method == 'POST':
        seat_number = request.POST.get('seat_number')
        username = request.session.get('username')
        
        # Update user's seat information in MongoDB
        collection.update_one({"username": username}, {"$set": {"seat": seat_number}})
        
        # Fetch updated seat info
        updated_user = collection.find_one({"username": username})
        
        return render(request, 'seat.html', {'user': updated_user})
    
    return render(request, 'seat.html')