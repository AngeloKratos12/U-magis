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
        for index in range(1,5):
            book = Books.objects.get(id=index)
            try:
                bookemprunted = models.Empruntes.objects.get(idBook=index)
                emprunted = 1
            except:
                emprunted = 0
            print(emprunted)
            idBook = book.id
            cotation = book.cotation
            titre = book.titre
            auteur = book.auteur
            bookshow = {
                    'cotation':cotation,
                    'titre':titre,
                    'auteur':auteur,
                    'idBook':idBook,
                    'emprunted':emprunted
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
            #cotation = request.POST['cotation']
            commentaire = request.POST['commentaire']
    
            if 'clicked_button' in request.POST:
                print(request.POST['clicked_button'])
                
                ##If the user clicked the borrow Button
                if  request.POST['clicked_button'] == 'Emprunter':
                    book = Books.objects.get(id=idBook)
                    cotation = book.cotation
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
                    
                ##If the user clicked the reservation button
                elif request.POST['clicked_button'] == 'Reserver':
                    book = Books.objects.get(id=idBook)
                    print(idBook)
                    titre = book.titre
                    categorie = book.categorie
                    cotation = book.cotation
                    bookEnCour = models.Empruntes.objects.get(idBook=idBook)
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
        books = models.Reserves.objects.all()
        list_book = []
        for book in books:
            userEnAttent = Users.objects.get(id=book.idUserEnAttent)
            dbbook = Books.objects.get(id=book.idBook)
            
            try:
                bookemprunte = models.Empruntes.objects.get(idBook=book.idBook)
                iduserbookemprunte = bookemprunte.idUser
                datelivraison = bookemprunte.dateEntre
                userEnCour = Users.objects.get(id=iduserbookemprunte)
                userEnCour = str(userEnCour.name) + ' ' + str(userEnCour.user_name)
                
            except:
                userEnCour = 'angelo'
                pass
            
            book = {
                'cotation' : book.cotation,
                'title' : book.titre,
                'UserEnAttent' : str(userEnAttent.name) + ' ' + str(userEnAttent.user_name),
                'UserEnCours' : userEnCour,
                'number_book' : dbbook.numero,
                'auteur' : dbbook.auteur,
                'etat' : dbbook.etat,
                'categorie' : dbbook.categorie,
                'dateLivraison':datelivraison,
                }
            
            list_book.append(book)

        #print(book)
        
    return render(request, 'reservation.html', context={'list_book':list_book})
    


def admin(request):
    '''
        Hello guys
    '''
    
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            print(request.POST.getlist('cocher'))
            for index in request.POST.getlist('cocher'):
                index = int(index)
                print(index)
                livree = models.Empruntes.objects.get(idBook = index)
                livree.delete()
                print('suppression avec succes...')
            
        books =models.Empruntes.objects.all()
        list_book = []
        for book in books:
            #userEnAttent = Users.objects.get(id=book.idUserEnAttent)
            user = Users.objects.get(id=book.idUser)
            user = str(user.name) + ' ' + str(user.user_name)
            dbbook = Books.objects.get(id=book.idBook)
            auteur_book = dbbook.auteur
            number_book = dbbook.numero
            etat = dbbook.etat
            categorie = dbbook.categorie
            
            book = {
                'idBook': dbbook.id,
                'number_book': number_book,
                'cotation' : book.cotation,
                'title' : book.titre,
                'auteur' : auteur_book,
                'etat' : etat,
                'categorie': categorie,
                'user' : user,
                'dateSortie' : book.dateSortie,
                'dateEntre': book.dateEntre
            }
            list_book.append(book)
        
    return render(request, 'borrow.html', context={'list_book':list_book})



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
    