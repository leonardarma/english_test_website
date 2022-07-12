from django.db import models

class Joueur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    ville = models.ForeignKey('Ville', on_delete=models.PROTECT)

class Verbe(models.Model):
    base_verbale = models.CharField(max_length=200)
    participe_passe = models.CharField(max_length=200)
    preterit = models.CharField(max_length=200)
    traduction = models.CharField(max_length=200)

class Partie(models.Model):
    score = models.IntegerField()
    joueur = models.ForeignKey('Joueur', on_delete=models.PROTECT, related_name="partie")
    

class Question(models.Model):
    reponse_participe_passe = models.CharField(max_length=200)
    reponse_preterit = models.CharField(max_length=200)
    date_envoie = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_reponse = models.DateTimeField(null=True)
    partie = models.ForeignKey('Partie', on_delete=models.PROTECT, related_name="question")
    verbe = models.ForeignKey('Verbe', on_delete=models.PROTECT)

class Ville(models.Model):
    nom = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=10)