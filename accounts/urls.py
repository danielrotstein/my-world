from django.urls import path


# Login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
]
