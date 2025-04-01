from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('page1/', views.page1, name="page1"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]


