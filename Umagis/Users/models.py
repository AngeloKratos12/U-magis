from django.db import models

# Create your models here.

class Users(models.Model):
    '''
        Les informations concernants les utilisateurs
    '''
    GENRE = (
        ('M','Mâle'),
        ('F', 'Femêlle'),
        ('O','Other'),
    )

    name = models.CharField(max_length=60)
    user_name = models.CharField(max_length=30)
    genre = models.CharField(max_length=1, choices=GENRE)
    matricule_number = models.CharField(max_length=10)
    classe = models.CharField(max_length=5)
    pass_word_hashed = models.CharField(max_length=15)
    contacte = models.CharField(max_length=25)
    image_path = models.CharField(max_length=50)


class AdminBibliotheque(models.Model):
    '''
        Les admnistrateurs du Bibliotheques
    '''
    GENRE = (
        ('M', 'Mâle'),
        ('F', 'Femêlle'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=60)
    user_name = models.CharField(max_length=30)
    genre = models.CharField(max_length=1, choices=GENRE)
    matricule_number = models.CharField(max_length=10)
    cin = models.CharField(max_length=13)
    pass_word_hashed = models.CharField(max_length=15)
    contacte = models.CharField(max_length=25)
    image_path = models.CharField(max_length=50)

