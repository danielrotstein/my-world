from django.shortcuts import render


# Models
from projects.models import Project


# Create your views here.


# ----------- Project List View --------------------------


def project_list_view(request):
    project_list = Project.objects.all()
    context = {"project_list": project_list}

    return render(request, "projects/list.html", context)
