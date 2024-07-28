from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home (request):

    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def dashboard_hom1(request):
    return HttpResponse("dashboard_hom1")

def dashboard_hom2(request):
    return HttpResponse("dashboard_hom2")

def dashboard_hom3(request):
    return HttpResponse("dashboard_hom3")

    


