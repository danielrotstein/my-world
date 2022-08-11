from django.shortcuts import render, redirect


# Models
from scuba_diving.models import ScubaDiving


# Forms
from scuba_diving.forms import ScubaCreateForm


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
    scuba_detail = ScubaDiving.objects.all()
    context = {
        "scuba_detail": scuba_detail
    }
    print(scuba_detail)
    return render(request, "interests/scuba/detail.html", context)


# -------- Scuba Create View ----------------

def scuba_create_view(request):
    if request.method == "POST":
        form = ScubaCreateForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
            return redirect("scuba_list")

    else:
        form = ScubaCreateForm()

    context = {
        "form": form
    }

    return render(request, "interests/scuba/create.html", context)


# -------- Equipment ---------------------------
# -------- Scuba List View ----------------


def equipment_list_view(request):
    equipment_list = ScubaDiving.objects.all()
    context = {
        "equipment_list": equipment_list
    }

    return render(request, "interests/scuba/equipment.html", context)
