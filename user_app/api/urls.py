from django.urls import path
from rest_framework.authtoken import views

from user_app.api.views import LogoutAPIView, RegistrationAPIView

urlpatterns = [
    path('login/', views.obtain_auth_token, name="login"),
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("logout/", LogoutAPIView.as_view(), name="logout")
]