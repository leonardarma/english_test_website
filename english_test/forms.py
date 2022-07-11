from django import forms
from .models import Ville

class ConnectForm(forms.Form):
    email = forms.CharField(label = "Email", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre Email ", "class":'inputChamp'}))
    password = forms.CharField(label = "Mot de passe", max_length=100,widget=forms.PasswordInput(attrs={'placeholder':"Votre Mot de Passe", "class":'inputChamp'}))
    
class InscriptForm(forms.Form):
    nom = forms.CharField(label= "Nom", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre Nom ", "class":'inputChamp'}))
    prenom = forms.CharField(label= "Prenom", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre Prenom ", "class":'inputChamp'}))
    email = forms.CharField(label= "Email", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre Email ", "class":'inputChamp'}))
    password = forms.CharField(label = "Password", widget=forms.PasswordInput(attrs={'placeholder':"Votre Mot de Passe ", "class":'inputChamp'}))
    niveau = forms.ChoiceField(choices=[(1,"Débutant"), (2,"Intermédiaire"), (3,"Expert")])
    ville = forms.ChoiceField(choices=[ (i.id, i.nom) for i in Ville.objects.all().order_by("nom")])
    
class QuestionForm(forms.Form):
    reponse_participe_passe = forms.CharField(label= "reponse_participe_passe", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Participe Passe", "class":'inputChamp'}))
    reponse_preterit = forms.CharField(label= "reponse_preterit", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Preterit", "class":'inputChamp'}))
    
