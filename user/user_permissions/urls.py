# from django.contrib import admin
from django.urls import path
from user_permissions import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('create_user',views.CreateUser.as_view(),name="create_user"),
    path('user_list',views.UserList.as_view(),name="user_list"),
]
