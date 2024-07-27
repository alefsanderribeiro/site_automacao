from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name="dashboard_home"),
    path('home2', views.dashboard_hom2, name="dashboard_home2"),
    path('table', views.exibir_tabela, name="minha_tabela"),
]