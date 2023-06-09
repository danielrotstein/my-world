from django.urls import path


# Login / Logout
from django.contrib.auth import views as auth_views


# Views (signup)
from accounts.views import signup


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", signup, name="signup"),
]
