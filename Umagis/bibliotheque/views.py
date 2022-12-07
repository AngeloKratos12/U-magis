from django.shortcuts import render
from Users.models import Users
from . import models
# Create your views here.

def addBook(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            ##Add the book to the base
            numero, auteur, titre, edition, annee  = request.POST['numero'], request.POST['auteur'], request.POST['titre'],request.POST['edition'],request.POST['annee']
            lieu, cotation, etat, observation, categorie = request.POST['lieu'],request.POST['cotation'],request.POST['etat'],request.POST['observation'],request.POST['categorie']
            addbook = models.Books(numero=numero, auteur=auteur, titre=titre, edition=edition, annee=annee,
                                   lieu=lieu, cotation=cotation, etat=etat, observation=observation, categorie=categorie)
            addbook.save()

        return render(request, 'addbook.html')
    else:
        return render(request, 'login.html')