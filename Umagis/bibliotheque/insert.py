from . import models

class AddBook:
    '''
        Ajout de donnée!!
    '''
    def __init__(self, book:dict):
        self.numero,self.auteur,self.titre ,self.edition,self.annee  = book["numero"],book["auteur"],book["titre"], book["edition"],book["annee"]
        self.lieu,self.cotation, self.etat,self.observation,self.categorie = book["lieu"],book["cotation"],book["etat"],book["observation"], book["categorie"]

    def addBook(self):
        '''
            ajout des livres!!
        '''
        book = models.Books(
            numero=self.numero, auteur=self.auteur, titre=self.titre, edition = self.edition,
            annee = self.annee, lieu=self.lieu, cotation =self.cotation, etat= self.etat,
            observation = self.observation, categorie =self.categorie
        )







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
        categorie = models.CharField(max_length=50)'''