from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='Home'),
    path('login/', views.login_view, name='Login'),
    path('signup/', views.signup_view, name='Signup'),
    path('email/', views.email_sender_view, name='Email'),
    path('logout/', views.logout_view, name='Logout'),
    path('activate/<str:user_>/<str:key_>/', views.activation_view, name='Profile'),

]
