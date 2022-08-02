from django.urls import path

# Views
from tasks.views import (
    task_create_view,
    task_list_view,
)


urlpatterns = [
    path("create/", task_create_view, name="create_task"),
    path("mine/", task_list_view, name="show_my_tasks"),
]
