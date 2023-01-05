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
        #print(request.GET.get('mat'))
        books = Books.objects.all()
        ##Si l'user fait de recherche
        
        if request.method == 'POST':
            motsclef = request.POST['recherche'] 
            
            motsclef = motsclef.lower() ##Mettre le mots clef en miniscule
            booksList = Books.objects.filter(titre__startswith = motsclef)
            print(len(motsclef))
            
            if len(motsclef) == 0:
                pass
            else:
                booksList2 = Books.objects.filter(titre__icontains = motsclef)
                
                for book in booksList2:
                    try:
                        bookemprunted = models.Empruntes.objects.get(idBook=book.id)
                        emprunted = 1
                        disponibilite = bookemprunted.dateEntre
                    except:
                        emprunted = 0
                        disponibilite = None
                        
                    idBook = book.id
                    cotation = book.cotation
                    titre = book.titre
                    auteur = book.auteur
                    bookshow = {
                            'cotation':cotation,
                            'titre':titre,
                            'auteur':auteur,
                            'idBook':idBook,
                            'emprunted':emprunted,
                            'disponible': disponibilite,
                        }
                    listbook.append(bookshow)
                
            for book in booksList:
                try:
                    bookemprunted = models.Empruntes.objects.get(idBook=book.id)
                    emprunted = 1
                    disponibilite = bookemprunted.dateEntre
                except:
                    emprunted = 0
                    disponibilite = None
                    
                idBook = book.id
                cotation = book.cotation
                titre = book.titre
                auteur = book.auteur
                bookshow = {
                        'cotation':cotation,
                        'titre':titre,
                        'auteur':auteur,
                        'idBook':idBook,
                        'emprunted':emprunted,
                        'disponible': disponibilite,
                    }
                listbook.append(bookshow)
            
            
            return render(request, 'biblio.html', context={'listbook':listbook,'nbr_book':len(listbook)})
                
                
                
                
                
            print(motsclef.lower())
        else:
            categorie = request.GET.get('categorie')
            print(categorie)
            if categorie == 'all':
                books = Books.objects.all()
                print('ALL')
            else:
                if categorie != 'None':
                    try:
                        #print(categorie)answer_list.append(dic_forum)
                        books = Books.objects.filter(categorie__startswith = categorie)
                        booksList2 = Books.objects.filter(categorie__icontains = categorie)
                        for book in booksList2:
                            try:
                                bookemprunted = models.Empruntes.objects.get(idBook=book.id)
                                emprunted = 1
                                disponibilite = bookemprunted.dateEntre
                            except:
                                emprunted = 0
                                disponibilite = None
                                
                            idBook = book.id
                            cotation = book.cotation
                            titre = book.titre
                            auteur = book.auteur
                            bookshow = {
                                    'cotation':cotation,
                                    'titre':titre,
                                    'auteur':auteur,
                                    'idBook':idBook,
                                    'emprunted':emprunted,
                                    'disponible': disponibilite,
                                }
                            listbook.append(bookshow)
                    except:
                        books = Books.objects.all()
            
            for book in books:
                try:
                    bookemprunted = models.Empruntes.objects.get(idBook=book.id)
                    emprunted = 1
                    disponibilite = bookemprunted.dateEntre.strftime("%B %d, 20%y")
                except:
                    emprunted = 0
                    disponibilite = None
                
            # print(emprunted)
                idBook = book.id
                cotation = book.cotation
                titre = book.titre
                auteur = book.auteur
                bookshow = {
                        'cotation':cotation,
                        'titre':titre,
                        'auteur':auteur,
                        'idBook':idBook,
                        'emprunted':emprunted,
                        'disponible': disponibilite,
                    }
                if bookshow in listbook:
                    pass
                else:
                    listbook.append(bookshow)
            
            
            
            return render(request, 'biblio.html', context={'listbook':listbook, 'nbr_book':len(listbook)})

    else:
        return render(request, 'login2.html')
    


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
            try:
               commentaire = request.POST['commentaire']
            except:
                commentaire = '**'
    
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
        return render(request, 'login2.html')


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
                userEnCour = '**'
                datelivraison = '**'
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
        
        return render(request, 'reservation.html', context={'list_book':list_book,'nbr_book':len(list_book)})
    else:
        return render(request, 'login2.html')
    


def admin(request):
    '''
        Hello guys
    '''
    
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        booklist =models.Empruntes.objects.all()
        list_book = []
        if request.method == 'POST':
            print(request.POST.getlist('cocher'))
            rechercher = request.POST['rechercher']
            select = request.POST['select']
            for index in request.POST.getlist('cocher'):
                index = int(index)
                print(index)
                livree = models.Empruntes.objects.get(idBook = index)
                livree.delete()
                print('suppression avec succes...')
            
            
            #print(select, rechercher)
            if len(rechercher) != 0:
                listId = []
                if select == 'etudiant':
                    etudiantname = Users.objects.filter(name__startswith = rechercher)
                    etudiantuser_name = Users.objects.filter(user_name__startswith = rechercher)
                    print(etudiantname, etudiantuser_name)
                    
                    if len(etudiantname) != 0 or len(etudiantuser_name) != 0:
                        booklist = []
                        for user in etudiantname:
                            
                            listId.append(user.id)
                            print(listId)
                          

                        for user in etudiantuser_name:
                            if user.id in listId:
                                pass
                            
                            else:
                                listId.append(user.id)

                        for userId in listId:
                            books = models.Empruntes.objects.filter(idUser=userId)
                            booklist.extend(books)
                    else:
                        pass
                
                elif select == 'titre':
                    booklist = models.Empruntes.objects.filter(titre__startswith = rechercher)
                    
                elif select == 'cotation':
                    booklist = models.Empruntes.objects.filter(cotation__startswith = rechercher)
                
                elif select == 'numero':
                    booklist = models.Empruntes.objects.filter(numero__startswith = rechercher)
                
                elif select == 'auteur':
                    booklist = models.Empruntes.objects.filter(cotation__startswith = rechercher)
            else:
                pass
        
        for book in booklist:
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
        return render(request, 'login2.html')
    