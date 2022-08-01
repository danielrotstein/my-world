from django.shortcuts import render, redirect


# Models
from projects.models import Project


# Login Required
from django.contrib.auth.decorators import login_required


# Forms
from projects.forms import ProjectCreateForm


# Create your views here.


# ----------- Project List View --------------------------


@login_required()
def project_list_view(request):
    project_list = Project.objects.filter(members=request.user)
    context = {"project_list": project_list}

    return render(request, "projects/list.html", context)


# ----------- Project Detail View --------------------------


@login_required()
def project_detail_view(request, pk):
    project_detail = Project.objects.get(pk=pk)
    context = {"project_detail": project_detail}

    return render(request, "projects/detail.html", context)


# ----------- Project Create View --------------------------

@login_required()
def project_create_view(request):
    if request.method == "POST":
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
            form.save_m2m()
            return redirect("show_project", create.pk)

    else:
        form = ProjectCreateForm()

    context = {"form": form}

    return render(request, "projects/create.html", context)
