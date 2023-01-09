from django.db import models

# Create your models here.

class Question(models.Model):
    '''
        Table des topic 
    '''
    question = models.CharField(max_length=500)
    idUser = models.IntegerField()
    about = models.CharField(max_length=200)
    detail = models.TextField()
    date = models.DateTimeField()