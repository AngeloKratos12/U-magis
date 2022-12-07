from django.db import models

# Create your models here.

class Books(models.Model):
    '''
        Table of all books at Vohijoky
    '''

    numero = models.CharField(max_length=6)
    auteur = models.CharField(max_length=30)
    titre = models.CharField(max_length=100)
    edition = models.CharField(max_length=10, blank=True)
    annee = models.IntegerField(blank=True)
    lieu = models.CharField(max_length=15, blank=True)
    cotation = models.CharField(max_length=10)
    etat = models.IntegerField()
    observation = models.CharField(max_length=20, blank=True)
    categorie = models.CharField(max_length=50)

#-----------------------------------------------------------------------------------------------------

class PhysiqueElectricite(models.Model):
    '''
        Table of all books physic and electricity
    '''

    numero = models.CharField(max_length=6)
    auteur = models.CharField(max_length=30)
    titre = models.CharField(max_length=100)
    edition = models.CharField(max_length=10, blank=True)
    annee = models.IntegerField(blank=True)
    lieu = models.CharField(max_length=15, blank=True)
    cotation = models.CharField(max_length=10)
    etat = models.IntegerField()
    observation = models.CharField(max_length=20, blank=True)