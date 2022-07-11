from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inscription', views.inscription, name="inscription"),
    path('jeu', views.jeu, name="jeu" ),
    path('final', views.final, name="final"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
]