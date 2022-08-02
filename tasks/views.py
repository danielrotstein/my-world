from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Models
from tasks.models import Task


# Forms
from tasks.forms import TaskCreateForm


# Login Required
from django.contrib.auth.decorators import login_required


# POST Requests
from django.views.decorators.http import require_http_methods




# Create your views here.

# ------------ Task List View -------------------------

@login_required()
def task_list_view(request):
    task_list = Task.objects.filter(assignee=request.user)
    context = {
        "task_list": task_list
    }

    return render(request, "tasks/list.html", context)


# ------------ Task Create View -------------------------

@login_required()
def task_create_view(request):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.assignee = request.user
            create.save()
            return redirect("show_project", create.project_id)

    else:
        form = TaskCreateForm()
    context = {
        "form": form
    }

    return render(request, "tasks/create.html", context)


# ------------ Task Update View -------------------------

@require_http_methods(["POST"])
def task_update_view(request):
    # Try working with this one
    # task_update = Task.objects.get(is_completed="True")

    is_completed = request.POST.get("is_completed")
    completed = Task.objects.get(id=is_completed)
    # assignee = request.user

    try:
        Task.objects.update(
            is_completed=completed,
            # assignee=assignee,
        )

    except Exception as error:
        raise error

    return redirect("show_my_tasks", pk=is_completed.id)
