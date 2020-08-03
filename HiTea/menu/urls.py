from django.contrib import admin
from django.urls import path
from . import views as menu_views

urlpatterns = [
    path('', menu_views.home, name='menu-home'),
    path('<str:product_type>/', menu_views.getMenuData, name='menu-search'),
]