from django.shortcuts import render, redirect

# Create your views here.

def defesa_civil(request):
    return render(request, "defesa_civil.html", {})

def guarda_municipal(request):
    return render(request, "guarda_municipal.html", {})

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

# Guarda Municipal
def secretaria_de_seguranca_urbana_cidadania(request):
    return render(request, "servicos_guarda_municipal/secretaria_de_seguranca_urbana_cidadania.html", {})

def solicitacao_de_guarnicao(request):
    return render(request, "servicos_guarda_municipal/solicitacao_de_guarnicao_para_evento.html", {})

def solicitacao_de_rondas(request):
    return render(request, "servicos_guarda_municipal/solicitacao_de_rondas_da_guarda_municipal.html", {})

def ligue_para_nos(request):
    return render(request, "servicos_guarda_municipal/ligue_para_nos.html", {})

def teatro_de_fantoches(request):
    return render(request, "servicos_guarda_municipal/teatro_de_fantoches.html", {})

def ouvidoria(request):
    return render(request, "servicos_guarda_municipal/ouvidoria.html", {})

def denuncie_aqui(request):
    return render(request, "servicos_guarda_municipal/denuncie_aqui.html", {})