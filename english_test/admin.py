from queue import Queue
from django.contrib import admin
from .models import Joueur, Verbe, Partie, Question, Ville

@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin): 
    search_fields = ['nom', 'code_postal']
    list_display = ['nom','code_postal']

admin.site.register(Joueur)
admin.site.register(Verbe)
admin.site.register(Partie)
admin.site.register(Question)