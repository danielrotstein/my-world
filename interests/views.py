from django.shortcuts import render, redirect


# Models
from interests.models import Interest


#Forms
from interests.forms import InterestCreateForm


# Create your views here.


# -------- Interest List View ----------------

def interest_list_view(request):
    interest_list = Interest.objects.all()
    context = {
        "interest_list": interest_list
    }

    return render(request, "interests/list.html", context)


# -------- Interest Detail View ----------------

def interest_detail_view(request, pk):
    interest_detail = Interest.objects.get(pk=pk)
    context = {
        "interest_detail": interest_detail
    }

    return render(request, "interests/detail.html", context)


# -------- Interest Create View ----------------

def interest_create_view(request):
    if request.method == "POST":
        form = InterestCreateForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
            return redirect("interest_list")

    else:
        form = InterestCreateForm()

    context = {"form": form}

    return render(request, "interests/create.html", context)







