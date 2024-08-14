from django.shortcuts import render, redirect

# Create your views here.

def seguranca(request):
    return render(request, "defesa_civil.html", {})

# Defesa Civil

def palestra(request):
    return render(request, "servicos_defesa_civil/palestra.html", {})

def registro(request):
    return render(request, "servicos_defesa_civil/registro_de_ocorrencia_e_desastre.html", {})

def vistoria(request):
    return render(request, "servicos_defesa_civil/solicitacao_de_vistorias_preventivas.html", {})

def alagamento(request):
    return render(request, "servicos_defesa_civil/alagamento.html", {})

def desmoronamento(request):
    return render(request, "servicos_defesa_civil/desmoronamento.html", {})