from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse("드디어 연결성공")
    context = {}
    return render(request, 'index.html', context)

def seat(request):
    #return HttpResponse("드디어 연결성공")
    context = {}
    return render(request, 'seat.html', context)