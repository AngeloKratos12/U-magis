from django.shortcuts import render, HttpResponse, redirect
from Users.models import Users
from bibliotheque.models import Books
from . import models

# Create your views here.

def biblio(request):
    '''
        ACCEUIL DE GESTION DE LIVRE!!
    '''
    
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        listbook = []
        for index in range(0,5):
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
    


def borrow(request):
    '''
        Envoie des informations des livres dans la BD!!
    '''
    
    #if user have e session
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        
        #if user pushed the submit button
        if request.method == 'POST':
            from datetime import datetime, timedelta
            
            idBook = request.POST['idBook']
            cotation = request.POST['cotation']
            commentaire = request.POST['commentaire']
    
            if 'clicked_button' in request.POST:
                print(request.POST['clicked_button'])
                
                ##If the user clicked the borrow Button
                if  request.POST['clicked_button'] == 'Emprunter':
                    book = Books.objects.get(id=idBook)
                    categorie = book.categorie
                    titre = book.titre
                    dateSortie = datetime.now()
                    dateEntre = dateSortie + timedelta(days=14, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
                    print(dateEntre)
                    '''
                        Envoie des informations vers la base de donnée
                    '''
                    addbook = models.Empruntes(idBook=idBook, cotation=cotation, titre=titre, categorie=categorie,
                                            idUser=logged_user_id, dateSortie=dateSortie, dateEntre=dateEntre,
                                            commentaire=commentaire)
                
                    addbook.save()
                    
                ##If the user clicked the reservatio button
                elif request.POST['clicked_button'] == 'Reserver':
                    book = Books.objects.get(id=idBook)
                    titre = book.titre
                    categorie = book.categorie
                    bookEnCour = models.Empruntes.objects.get(id=idBook)
                    idUserEnCour = bookEnCour.idUser
                    
                    ##send the information to database
                    makereservation = models.Reserves(idBook=idBook, cotation=cotation,titre=titre,categorie=categorie,
                                                    idUserEnAttent=logged_user_id, idUserEnCour=idUserEnCour, commentaire=commentaire)
                    makereservation.save()
                
                else:
                    pass
                    
            return redirect('books')
        
        
        else:
            return render('books')

    #If user have not yet a compte
    else:
        return render(request, 'login.html')


def reservation(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        book =models.Reserves.objects.all()
        #print(book)
        
    return render(request, 'reservation.html', context={'book':book})
    


def admin(request):
    '''
        Hello guys
    '''
    
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        book =models.Empruntes.objects.all()
        #print(book)
        
    return render(request, 'borrow.html', context={'book':book})

def addBook(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            ##Add the book to the base
            numero, auteur, titre, edition, annee  = request.POST['numero'], request.POST['auteur'], request.POST['titre'],request.POST['edition'],request.POST['annee']
            lieu, cotation, etat, observation, categorie = request.POST['lieu'],request.POST['cotation'],request.POST['etat'],request.POST['observation'],request.POST['categorie']
            addbook = Books(numero=numero, auteur=auteur, titre=titre, edition=edition, annee=annee,
                                   lieu=lieu, cotation=cotation, etat=etat, observation=observation, categorie=categorie)
            addbook.save()

        return render(request, 'addbook.html')
    else:
        return render(request, 'login.html')
    