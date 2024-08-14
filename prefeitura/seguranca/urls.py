from django.urls import path
from . import views

urlpatterns = [
    # path("", views., name=""),
    path("defesa-civil/", views.seguranca, name="seguranca"),
    path("palestras-para-instituições-de-ensino/", views.palestra, name="palestra"),
    path("registro-de-ocorrencia-e-desastre", views.registro, name="registro"),
    path("solicitacao-de-vistorias-preventivas", views.vistoria, name="vistoria"),
    path("alagamento", views.alagamento, name="alagamento"),
    path("desmoronamento", views.desmoronamento, name="desmoronamento"),
]