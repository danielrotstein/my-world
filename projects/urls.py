from django.urls import path


# Views
from projects.views import (
    project_list_view,
)


urlpatterns = [
    path("", project_list_view, name="list_projects"),
]
