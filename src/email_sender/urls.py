from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='Home'),
    path('login/', views.home_view, name='Home'),
    path('signup/', views.home_view, name='Home'),
    path('email/', views.home_view, name='Home'),

]
