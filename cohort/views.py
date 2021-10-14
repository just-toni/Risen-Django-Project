from django.shortcuts import render, redirect

# Create your views here.
from cohort.forms import CohortCreationForms
from cohort.models import Cohort


def hello_world(request):
    return render(request, "hello_world.html")

def get_all_cohorts(request):
    cohorts = Cohort.object.all()
    print(cohorts)
    context= {
        "cohorts": cohorts
    }
    return render(request, "cohorts.html", context)

def create_cohort(request):
    form = CohortCreationForms()
    if request.method == "POST":
        cohort_form = CohortCreationForms(request.POST)
        if cohort_form.is_valid():
            cohort_form.save()
            return redirect('cohorts')
        else:
            context = {
                "error": cohort_form.errors
            }
        return render(request, "error_page.html", context)
    return render(request, "create_cohort.html", context={"form", form})

def create_page(request):
    return render(request, "some.html")

def get_a_cohort(request, pk):
    try:
        cohort = Cohort.objects.get(id=pk)
        return render(request, "get_a_cohort.html", {"cohort" : cohort})
    except Cohort.DoesNotExist:
        context = {
            "error" : "This Cohort does not exist."
        }
        return render(request, "error_page.html", context)
