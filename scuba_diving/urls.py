from django.urls import path


# Views
from scuba_diving.views import (
    scuba_list_view,
    equipment_list_view,
    scuba_detail_view,
    scuba_create_view,
    scuba_update_view,
)


urlpatterns = [
    path("interests/scuba/", scuba_list_view, name="scuba_list"),
    path("interests/scuba/equipment", equipment_list_view,
         name="equipment_list"),
    path("interests/scuba/<int:pk>/", scuba_detail_view, name="scuba_detail"),
    path("interests/scuba/create", scuba_create_view, name="scuba_create"),
    path("interests/scuba/<int:pk>/edit/", scuba_update_view,
         name="scuba_edit"),
]
