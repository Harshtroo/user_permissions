# from django.contrib import admin
from django.urls import path
from user_permissions import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('login/',views.Login.as_view(),name="login"),
    path('create_user/',views.CreateUser.as_view(),name="create_user"),
    path('user_list/',views.UserList.as_view(),name="user_list"),
    path('user_edit/<int:pk>/',views.UserEdit.as_view(),name="user_edit"),
    path('user_delete/<int:pk>/',views.UserDelete.as_view(),name="user_delete"),
    path('add_item/',views.AddItems.as_view(),name= 'add_items'),
    path('items_list/',views.ItemsList.as_view(),name="items_list"),
    path('logout/',views.Logout.as_view(),name="logout"),
]
