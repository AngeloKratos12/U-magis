from django.http import HttpResponse
from django.shortcuts import render, redirect
from Users.models import Users


def home(request):
    user = Users.objects.get(id=1)
    user = user.contacte
    return render(request, 'home.html')


def home2(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        return render(request, 'home2.html')
    
    else:
        return render(request, 'home.html')

def login(request):
    user = Users.objects.get(id=1)
    user = user.pass_word_hashed
    return render(request, 'login2.html')


def verify(request):
    '''
        verification de l'indentifiant!!
    '''

    if request.method == 'POST':
        #get the matricule enter by user
        matricule = request.POST['matricule']
        password = request.POST['password']
        try:
            '''
                Verification si le numero matricule entrée est dans DB.
            '''
            logged_user = Users.objects.get(matricule_number = matricule)
            ##get the pass word in database
            logged_user_password = logged_user.pass_word_hashed
            ##verification si le mots de pass se rensemble
            if password == logged_user_password:
                ##Mots de pass correcte
                request.session['logged_user_id'] = logged_user.id
                return render(request, 'home2.html', context={'logged_user' : logged_user})
            else:
                #Si le mots de pass est incorecte
                return  HttpResponse('ERROR PASSWORD')
        except:
            ##Matricule n'existe pas dans la base!!
            return HttpResponse('ERROR MATRICULE')



def logout(request):
    '''
        PAge de deconnexion
    '''

    if 'logged_user_id' in request.session:
        del request.session['logged_user_id']
    return render(request, 'home.html')



