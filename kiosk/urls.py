from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seat.html', views.seat, name='seat'),
    path('auth/login', views.login, name='login'),
    path('auth/register', views.register, name='register'),
    path('auth/logout', views.logout, name='logout'),
    path('auth/check', views.check_login_status, name='check_login_status'),
    path('seat/select', views.select_seat, name='select_seat'),
    path('seat/deselect', views.deselect_seat, name='deselect_seat'),
    path('seat/seats', views.fetch_seat_info, name='fetch_seat_info'),
]
