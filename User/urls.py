from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('user/new/', views.user_new, name='user_new'),
    path('', views.user_list, name='user_list'),
]