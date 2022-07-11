from time import time
from random import choice
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from english_test.models import Joueur, Partie, Verbe, Ville, Question
from .forms import ConnectForm, InscriptForm, QuestionForm

def index(request):
    if request.POST:
        form = ConnectForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                joueur = Joueur.objects.get(email = email)
                if check_password(password, joueur.password):
                    request.session['joueur_id'] = joueur.id
                    return HttpResponseRedirect('/english_test/jeu')
                else:
                    raise
            except:
                return HttpResponseRedirect('/english_test/error')
    else:
        form = ConnectForm()
    context = {
        "form" : form
    }
    return render(request, 'english_test/index.html', context)

def inscription(request):
    if request.POST:
        form = InscriptForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data["nom"]
            prenom = form.cleaned_data["prenom"]
            email = form.cleaned_data["email"]
            password = make_password( form.cleaned_data["password"] )
            ville = Ville.objects.get(pk= form.cleaned_data["ville"])
            print("yo")
            joueur = Joueur(nom = nom, prenom = prenom, email = email, password=password, ville=ville)
            joueur.save()
            return HttpResponseRedirect('/english_test/')
    else:
        form = InscriptForm()
    context = {
        "form" : form
    }
    return render(request, 'english_test/inscription.html', context)

def jeu(request):
    
    try:
        joueur = Joueur.objects.get(pk=request.session["joueur_id"])
    except:
        return HttpResponseRedirect('/english_test/')
    context = {"joueur": joueur}
    
    # if joueur.partie.count()>0:
    #     partie = joueur.partie.latest('id')
    #     print(partie.creatime.timestamp()+60>time())
    #     if partie.creatime.timestamp()+60>time():
    #         return HttpResponseRedirect('/english_test/final')
    # else:
    #     partie = Partie(joueur=joueur, score = 0)
    #     partie.save()
        
    # context["partie"] = partie
    
    print(joueur.partie.latest('question') )
        
        
    
    if request.POST:
        form = QuestionForm(request.POST)
        if form.is_valid():
            
            reponse_participe_passe = form.cleaned_data["reponse_participe_passe"]
            reponse_preterit = form.cleaned_data["reponse_preterit"]
    else:
        try:
            end = joueur.partie.latest('question').question.first()
        except:
            pass
        
        partie = Partie(joueur = joueur, score = 0)
        partie.save()
        verbe = choice(list(Verbe.objects.all()))
        question = Question(verbe = verbe, partie = partie)
        question.save()
            
            

    return render(request, 'english_test/jeu.html', context)

def final(request):
    try:
        joueur = Joueur.objects.get(pk=request.session["joueur_id"])
        max_lvl = joueur.partie.latest('score').score
        context = {
            "joueur": joueur,
            "max_lvl": max_lvl,
        }
    except:
        return HttpResponseRedirect('/english_test/')
    return render(request, 'english_test/fin.html', context)

def deconnexion(request):
    del request.session["joueur_id"]
    return HttpResponseRedirect('/english_test/')

# Create your views here.
