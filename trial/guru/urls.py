from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[path('signup',views.zxc),
				path('login',views.loginform),
				path('data',views.data),
				path('logout',views.logout),
				path('home',views.Home),
				path('',views.Home),
				path('dashboard',views.dashBoard),
				path('update',views.updateData),]




