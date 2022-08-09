from django.urls import path

from intro.views import intro_list_view


urlpatterns = [
    path("", intro_list_view, name="intro"),
]
