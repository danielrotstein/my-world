from django.shortcuts import render, redirect


# Models
from scuba_diving.models import ScubaDiving


# Forms
from scuba_diving.forms import (
    ScubaCreateForm,
    ScubaUpdateForm,
)


# Create your views here.


# -------- Scuba List View ----------------

def scuba_list_view(request):
    scuba_list = ScubaDiving.objects.all()
    context = {
        "scuba_list": scuba_list
    }

    return render(request, "interests/scuba/list.html", context)


# -------- Scuba Detail View ----------------

def scuba_detail_view(request, pk):
    scuba_detail = ScubaDiving.objects.get(pk=pk)
    context = {
        "scuba_detail": scuba_detail
    }
    
    return render(request, "interests/scuba/detail.html", context)


# -------- Scuba Create View ----------------

def scuba_create_view(request):
    if request.method == "POST":
        form = ScubaCreateForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
            return redirect("scuba_detail", create.pk)

    else:
        form = ScubaCreateForm()

    context = {
        "form": form
    }

    return render(request, "interests/scuba/create.html", context)


# -------- Scuba List View ----------------

def scuba_update_view(request, pk):
    scuba_update = ScubaDiving.objects.get(pk=pk)
    if request.method == "POST":
        form = ScubaUpdateForm(request.POST, instance=scuba_update)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect("scuba_list")

    else:
        form = ScubaUpdateForm()
    
    context = {
        "form": form
    }

    return render(request, "interests/scuba/edit.html", context)









# -------- Equipment ---------------------------
# -------- Scuba List View ----------------


def equipment_list_view(request):
    equipment_list = ScubaDiving.objects.all()
    context = {
        "equipment_list": equipment_list
    }

    return render(request, "interests/scuba/equipment.html", context)
