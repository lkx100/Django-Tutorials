from django.urls import path
from . import views   # . is called current directory

urlpatterns = [
    path('', views.all_chai, name = 'all_chai_home'),   # localhost: 8000/chai
    path('order/', views.order, name = 'order'),        # localhost: 8000/chai/order
]