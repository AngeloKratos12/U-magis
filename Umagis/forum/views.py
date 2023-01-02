from django.shortcuts import render
from Users.models import Users
# Create your views here.

def forum_home(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        return render(request, 'forum.html')
    
    else:
        return render(request, 'home.html')



def addtopic(request):
    '''
        Add topic to database
    '''
    