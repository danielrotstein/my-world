from django.shortcuts import render, redirect


# Models
from tasks.models import Task


# Forms
from tasks.forms import TaskCreateForm


# Login Required
from django.contrib.auth.decorators import login_required


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
