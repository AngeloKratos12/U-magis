from django.db import models

# Create your models here.

class Empruntes(models.Model):
    '''
        Une table qui contient tous les infos du livre emprunté par les etudiants
    '''

    idBook = models.IntegerField()
    cotation = models.CharField(max_length=10)
    titre = models.CharField(max_length=100)
    categorie = models.CharField(max_length=50)
    idUser = models.IntegerField()
    dateSortie = models.DateTimeField()
    dateEntre = models.DateTimeField()
    commentaire = models.TextField(blank=True)
    

#-------------------------------------------------------------------------------------
    
    
#-------------------------------------------------------------------------------------

class Reserves(models.Model):
    '''
        Une table qui contient les reservation du livre
    '''

    idBook = models.IntegerField()
    cotation = models.CharField(max_length=10)
    titre = models.CharField(max_length=100)
    categorie = models.CharField(max_length=50)
    idUserEnAttent = models.IntegerField()
    idUserEnCour = models.IntegerField()
    commentaire = models.TextField(blank=True)
