from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('page1', views.dashboard_hom2, name="dash_pg1"),
    path('page2', views.dashboard_hom2, name="dash_pg2"),
    path('page3', views.dashboard_hom2, name="dash_pg3"),
]