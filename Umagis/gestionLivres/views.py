from django.shortcuts import render, HttpResponse
from Users.models import Users
from bibliotheque.models import Books
from . import models

# Create your views here.

def biblio(request):
    '''
        ACCEUI DE GESTION DE LIVRE!!
    '''
    
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        listbook = []
        for index in range(1,3):
            book = Books.objects.get(id=index)
            idBook = book.id
            cotation = book.cotation
            titre = book.titre
            auteur = book.auteur
            bookshow = {
                    'cotation':cotation,
                    'titre':titre,
                    'auteur':auteur,
                    'idBook':idBook
                }
            listbook.append(bookshow)
            
        return render(request, 'biblio.html', context={'listbook':listbook})

    else:
        return render(request, 'login.html')


def makereservation(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
    
    return render(request, 'reservation.html')



def borrow(request):
    '''
        Envoie des informations des livres dans la BD!!
    '''

    
    
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            from datetime import datetime, timedelta
            
            idBook = request.POST['idBook']
            cotation = request.POST['cotation']
            commentaire = request.POST['commentaire']
            
            book = Books.objects.get(id=str(idBook))
            categorie = book.categorie
            titre = book.titre
            dateSortie = datetime.now()
            dateEntre = dateSortie + timedelta(days=14, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
            print(dateEntre)
            addbook = models.Empruntes(idBook=idBook, cotation=cotation, titre=titre, categorie=categorie,
                                       idUser=logged_user_id, dateSortie=dateSortie, dateEntre=dateEntre,
                                       commentaire=commentaire)
        
            addbook.save()
            return HttpResponse(cotation)

        else:
            return render(request, 'biblio.html')

    else:
        return render(request, 'login.html')
    
    
    
    
    '''
    idBook = models.IntegerField()
    cotation = models.CharField(max_length=10)
    titre = models.CharField(max_length=100)
    categorie = models.CharField(max_length=50)
    idUser = models.IntegerField()
    dateSortie = models.DateTimeField()
    dateEntre = models.DateTimeField()
    commentaire = models.TextField(blank=True)
    '''