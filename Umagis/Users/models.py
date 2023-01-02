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


class Students(models.Model):
    """
        potfolio des étudiants
    """
    idstudent = models.IntegerField()
    post = models.CharField(max_length=60)
    niveau = models.CharField(max_length=60)
    work = models.CharField(max_length=60)
    about_me1 = models.TextField()
    about_me2 = models.TextField()
    photo_link = models.CharField(max_length=60)

class StudentCompetences(models.Model):
    '''
        Table des compétences des étudiants
    '''
    idstudent = models.IntegerField()
    competence_title = models.CharField(max_length=50)
    competences = models.CharField(max_length=100)

class StudentExperience(models.Model):
    '''
        Table des experiences des étudiants
    '''
    idstudent = models.IntegerField()
    entreprise = models.CharField(max_length=20)
    poste = models.CharField(max_length=60)
    date_debut  = models.DateField()
    date_fin = models.DateField()

class StudentFormation(models.Model):
    '''
        Table des Formations des étudiants
    '''
    idstudent = models.IntegerField()
    ecole = models.CharField(max_length=20)
    plusinfo = models.CharField(max_length=60)
    date_debut  = models.DateField()
    date_fin = models.DateField()

class Realisation(models.Model):
    '''
        Tables des réalisations faits par les étudiants
    '''
    idstudent = models.IntegerField()
    name = models.CharField(max_length=60)
    description = models.TextField()
    support_link = models.TextField(max_length=60)
    link_net = models.CharField(max_length=80)


class StudentPrix(models.Model):
    '''
        Table des Prix obtenue par les étudiants
    '''
    idstudent = models.IntegerField()
    prix = models.CharField(max_length=20)
    plusinfo = models.CharField(max_length=200)
    date  = models.DateField()

class contactes(models.Model):
    '''
        contacte linkof the student
    '''
    idstudent = models.IntegerField()
    link = models.CharField(max_length=60)

