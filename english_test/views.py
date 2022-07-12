from datetime import datetime
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
    
    if request.method == 'POST':
        partie = joueur.partie.latest('question__date_envoie')
        first_question = partie.question.earliest('date_envoie')
        if first_question.date_envoie.timestamp()+60>time():
            return HttpResponseRedirect('/english_test/final')
        
        form = QuestionForm(request.POST)
        if form.is_valid():
            reponse_participe_passe = form.cleaned_data["reponse_participe_passe"]
            reponse_preterit = form.cleaned_data["reponse_preterit"]
            date_reponse = datetime.now()
            question = joueur.partie.latest('question__date_envoie').question.latest('date_envoie')
            question.reponse_participe_passe = reponse_participe_passe
            question.reponser_preterit = reponse_preterit
            question.date_reponse = date_reponse
            question.save()
            if question.verbe.participe_passe == reponse_participe_passe and question.verbe.preterit == reponse_preterit:
                partie.score += 1
                partie.save()
                return HttpResponseRedirect('/english_test/jeu')
            else:
                print(question.verbe.traduction)
                print(question.verbe.participe_passe)
                print(reponse_participe_passe)
                return HttpResponseRedirect('/english_test/final')
            
    elif request.method == 'GET':
        form = QuestionForm()
        print(joueur.partie.latest('question').question.earliest('date_envoie').date_envoie.timestamp()-60<time())
        if joueur.partie.latest('question').question.earliest('date_envoie').date_envoie.timestamp()-60<time():
            partie = joueur.partie.latest('question')
            print(partie.score)
            verbe = choice(list(Verbe.objects.all()))
            question = Question(verbe = verbe, partie = partie)
            question.save()
        else:
            print(partie.score)
            partie = Partie(joueur = joueur, score = 0)
            partie.save()
            verbe = choice(list(Verbe.objects.all()))
            question = Question(verbe = verbe, partie = partie)
            question.save()
    best = joueur.partie.latest("score").score
    context = {
        'partie':partie,
        'form':form,
        "joueur": joueur,
        'question':question,
        'best':best,
        }
    return render(request, 'english_test/jeu.html', context)

def final(request):
    try:
        joueur = Joueur.objects.get(pk=request.session["joueur_id"])
        last_question = joueur.partie.latest("question__date_envoie").question.latest("date_envoie")
        best = joueur.partie.latest('score').score
        context = {
            "joueur": joueur,
            "best": best,
            "last_question": last_question,
        }
    except:
        return HttpResponseRedirect('/english_test/')
    return render(request, 'english_test/fin.html', context)

def deconnexion(request):
    del request.session["joueur_id"]
    return HttpResponseRedirect('/english_test/')

# Create your views here.
