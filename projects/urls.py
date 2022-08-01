from django.urls import path


# Views
from projects.views import (
    project_list_view,
    project_detail_view,
)


urlpatterns = [
    path("", project_list_view, name="list_projects"),
    path("<int:pk>/", project_detail_view, name="show_project"),
]
