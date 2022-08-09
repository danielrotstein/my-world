from django.urls import path

from interests.views import interest_list_view

urlpatterns = [
    path("", interest_list_view, name="interest_list")
]
