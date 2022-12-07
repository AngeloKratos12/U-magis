from django.shortcuts import render, HttpResponse
from Users.models import Users
from bibliotheque.models import Books

# Create your views here.

def biblio(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        return render(request, 'biblio.html')

    else:
        return render(request, 'login.html')


def makereservation(request):
    return render(request, 'reservation.html')



def borrow(request):
    '''
        fonction!!!!
    '''


    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':

            return HttpResponse('YES')

        else:
            return render(request, 'biblio.html')

    else:
        return render(request, 'login.html')