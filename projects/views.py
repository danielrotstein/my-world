from django.shortcuts import render


# Models
from projects.models import Project


# Login Required
from django.contrib.auth.decorators import login_required


# Create your views here.


# ----------- Project List View --------------------------


@login_required()
def project_list_view(request):
    project_list = Project.objects.filter(members=request.user)
    context = {"project_list": project_list}

    return render(request, "projects/list.html", context)
