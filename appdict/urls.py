from django.urls import path

from . import views

urlpatterns = [
   path("", views.consulta_termo, name="consulta-termo"),
]