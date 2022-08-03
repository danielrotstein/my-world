from django.shortcuts import render, redirect

# Models
from tasks.models import Task


# Forms
from tasks.forms import (
    TaskCreateForm,
    TaskUpdateForm,
)


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


# ------------ Task Update View -------------------------

@login_required()
def task_update_view(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.is_completed = True
            task.save()
            return redirect("show_my_tasks")

    else:
        form = TaskUpdateForm(instance=task)

    context = {
        "form": form
    }

    return render(request, "tasks/list.html", context)


# class UpdatedView(UpdateView):
#     model = ....
#     template_name = "fgdgfg"
#     fields = [
#         "mane",
#     ]

#     def form_valid(self, request):
#         form.is_valid()