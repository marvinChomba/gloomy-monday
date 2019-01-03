from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Job
from .forms import EditForm

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    form = EditForm()

    filters = {
        "time": None,
        "category": None,
        "location":None
    }

    if "time" in request.GET and request.GET["time"]:
        filters["time"] = (request.GET.get("time"))
    else:
        filters["time"] = (None)

    if "location" in request.GET and request.GET["location"]:
        filters["location"] = request.GET.get("location")
    else:
        filters["location"] = None
    
    if "category" in request.GET:
        filters["category"] = request.GET.get("category")
    else:
        filters["category"] = None

    if filters["location"] and filters["time"] and filters["category"]:
        jobs = Job.objects.filter(location__id = filters["location"],time = filters["time"],category__id = filters["category"])
    elif filters["time"] and filters["location"]:
        jobs = Job.objects.filter(location__id=filters["location"], time=filters["time"])
    elif filters["time"] and filters["category"] != "":
        jobs = Job.objects.filter(category__id=filters["category"], time=filters["time"])
    elif filters["category"] != "" and filters["location"]:
        jobs = Job.objects.filter(location__id=filters["location"], category__id=filters["category"])
    elif filters["category"]:
        jobs = Job.objects.filter(category__id = filters["category"])
    elif filters["time"]:
        jobs = Job.objects.filter(time=filters["time"])
    elif filters["location"]:
        jobs = Job.objects.filter(location__id=filters["location"])
    else:
        jobs = Job.objects.all()

    print(filters)

    context = {
        "jobs": jobs,
        "form": form,
    }



    return render(request,"jobs/index.html",context)

def single_job(request,id):
    job = get_object_or_404(Job,id=id)

    context = {
        "job":job
    }

    return render(request,"jobs/job.html",context)

    
