from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import subprocess

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


def exibir_tabela(request):
    # Suponha que você tenha um DataFrame chamado 'meu_dataframe'

    # Caminho para o executável do ambiente virtual (python.exe)
    caminho_venv = r'..\automatizar\.venv\Scripts\python.exe'
    arquivo = r"..\automatizar\main.py"
    # Comando para ativar o ambiente virtual e executar o script
    comando = f'{caminho_venv} {arquivo}'

    # Executa o comando
    print("Rodando Script")
    result = subprocess.run([caminho_venv, arquivo], capture_output=True, text=True, shell=True)
    print(result.stdout)
    meu_dataframe = pd.DataFrame({
        'Nome': ['Alice', 'Bob', 'Carol'],
        'Idade': [25, 30, 22]
    })


    # Converta o DataFrame em HTML
    tabela_html = meu_dataframe.to_html()

    return render(request, 'dashboard/minha_tabela.html', {'tabela_html': tabela_html})