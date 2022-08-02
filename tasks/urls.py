from django.urls import path

# Views
from tasks.views import task_create_view


urlpatterns = [
    path("create/", task_create_view, name="create_task"),
]
