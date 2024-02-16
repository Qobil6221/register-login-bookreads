from django.urls import path
from apps.users.views import UserLoginView, UserRegisterView 


path('register/', UserRegisterView.as_view(), name="register-page"),
path('login/', UserLoginView.as_view(), name="login-page"),