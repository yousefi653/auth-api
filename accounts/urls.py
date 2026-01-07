from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path("accounts/register/", views.Register.as_view()),
    path("accounts/login/", views.Login.as_view()),
    path("accounts/refresh/", TokenRefreshView.as_view()),
    path("accounts/logout/", views.Logout.as_view()),
    path("accounts/me/", views.MeView.as_view()),
]
