from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add', views.add, name = 'add'),
    path('greet', views.greet, name = 'greet'),
    path('dashboard/', views.dashboard, name = 'dashboard')
]