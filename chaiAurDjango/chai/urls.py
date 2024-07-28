from django.urls import path
from . import views   # . is called current directory

urlpatterns = [
    path('', views.all_chai, name = 'all_chai_home'),   # localhost: 8000/chai
    path('order/', views.order, name = 'order'),        # localhost: 8000/chai/order
    path('<int:chai_id>/', views.chai_details, name = 'chai_details')   # localhost: 8000/chai/24
]