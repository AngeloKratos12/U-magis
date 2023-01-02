from django.shortcuts import render
from Users.models import Users
from forum.models import Forum, Answer
from datetime import datetime
# Create your views here.

def forum_home(request):
    '''
        Select all Answer and Forum!!
    '''
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        
        allforum = Forum.objects.all()
        allanswer = Answer.objects.all()
        
        forum_list = []
  
        
        for forum in allforum:
            topic = forum.topic
            idUser = forum.idUser
            forum_name = forum.forum
            date = forum.date
            
            dic_forum = {
                'topic' : topic,
                'idUser' : idUser,
                'forum': forum_name,
                'date' : date
            }
            
            forum_list.append(dic_forum)
        
        answer_list = []
        for answer in allanswer:
            idtopic = answer.idtopic
            idrepondeur = answer.idrepondeur
            reponse = answer.reponse
            date = answer.date
            dic_answer = {
                'idtopic' : idtopic,
                'idrepondeur' : idrepondeur,
                'reponse' : reponse,
                'date' : date 
            }
            answer_list.append(dic_answer)
            
        
        
        
        
        
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


