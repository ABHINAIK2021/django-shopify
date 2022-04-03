from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sales/', views.sales, name='sales'),
    path('purchases/', views.purchases, name='purchases'),
    path('inventory/', views.inventory, name='inventory'),
]