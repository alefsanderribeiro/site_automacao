from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home (request):

    return HttpResponse("Home")

def dashboard(request):
    return HttpResponse("Dashboard")

def dashboard_home(request):

    return HttpResponse("DashBoard Home")


def dashboard_hom2(request):
    nomes = ["Alefe", "Geiss", "Veronica"]
    return render(request, "dashboard/dashboard.html", {"nomes":nomes})