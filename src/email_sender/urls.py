from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='Home'),
    path('login/', views.login_view, name='Home'),
    path('signup/', views.signup_view, name='Home'),
    path('email/', views.email_sender_view, name='Home'),

]
