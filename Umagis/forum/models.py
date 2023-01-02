from django.db import models

# Create your models here.

class Forum(models.Model):
    '''
        Table des topic 
    '''
    topic = models.CharField(max_length=200)
    idUser = models.IntegerField()
    forum = models.CharField(max_length=20)
    date = models.DateTimeField()


class Answer(models.Model):
    '''
        tables des reponses
    '''
    idtopic = models.IntegerField()
    idrepondeur = models.IntegerField()
    reponse = models.TextField()
    date = models.DateTimeField()
    