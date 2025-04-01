from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import home, create_post, delete_post, page1

urlpatterns=[
    path('', views.home, name="home"),
    path('page1/', page1, name="page1"),
    path('create/', create_post, name='create_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout')
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]


