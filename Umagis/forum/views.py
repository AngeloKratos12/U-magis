from django.shortcuts import render
from Users.models import Users
from forum.models import Forum, Answer
from datetime import datetime
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
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            topic = request.POST['topic']
            idUser = logged_user_id
            forum = request.POST['forum']
            date = datetime.now()
            addtopic = Forum(topic=topic, idUser=idUser, forum=forum, date=date)
            addtopic.save()
        else:
            pass
    
        return render(request, 'forum.html')
        
    else:
        render(request, 'login2.html')
            


def addanswer(request):
    '''
        Add the answer to DB
    '''
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            reponse = request.POST['reponse']
            idrepondeur = logged_user_id
            idtopic = request['idtopic']
            date = datetime.now()
            addanswer = Answer(idtopic=idtopic, idrepondeur=idrepondeur, reponse=reponse, date=date)
            addanswer.save()
        else:
            pass
        
        return render(request, 'forum.html')
    else:
        return render(request, 'login2.html')


