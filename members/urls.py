from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('members/', views.members, name='members'),
    path('home/', views.home, name='home'),
    path('adduser/', views.adduser, name='adduser')

]
