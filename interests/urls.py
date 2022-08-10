from django.urls import path

from interests.views import (
    interest_list_view,
    interest_detail_view,
    equipment_detail_view,
    interest_create_view,
)

urlpatterns = [
    path("", interest_list_view, name="interest_list"),
    path("<int:pk>/", interest_detail_view, name="interest_detail"),
    path("<int:pk>/equipment", equipment_detail_view, name="equipment_detail"),
    path("create/", interest_create_view, name="interest_create"),
]
