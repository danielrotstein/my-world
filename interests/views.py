from django.shortcuts import render

from interests.models import Interest

# Create your views here.


def interest_list_view(request):
    interest_list = Interest.objects.all()
    context = {
        "interest_list": interest_list
    }

    return render(request, "interests/list.html", context)