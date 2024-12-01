from django.urls import path
from EcomApp import views


urlpatterns = [
   path('', views.Home, name='home'),
   path('product/<int:id>/', views.product_single, name='product_single'),
]