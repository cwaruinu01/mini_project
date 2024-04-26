from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('members/', views.members, name='members'),
    path('home/', views.home, name='home'),
    path('adduser', views.adduser, name='adduser'),
    path('edituser/<id>/', views.edituser, name='edituser'),
    path('updatuser/<id>/', views.updateuser, name='updateuser'),
    path('deleteuser/<id>/', views.deleteuser, name='deleteuser'),
]
