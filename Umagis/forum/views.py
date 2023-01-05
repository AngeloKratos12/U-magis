from django.shortcuts import render, redirect, HttpResponse
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
        print(allforum)
        forum_list = []
    
        
        answer_list = []
        if len(allanswer) != 0:
            for answer in allanswer:
                for forum in allforum:
                    topic = forum.topic
                    idUser = forum.idUser
                    forum_name = forum.forum
                    date = forum.date
                    print(forum.id)
                    if forum.id == answer.idtopic: 
                        print(forum.id)
                        idtopic = answer.idtopic
                        idrepondeur = answer.idrepondeur
                        reponse = answer.reponse
                        date = answer.date
                        dic_forum = {
                                'id' : forum.id,
                                'topic' : topic,
                                'idUser' : idUser,
                                'forum': forum_name,
                                'date' : date
                            }
                        dic_answer = {
                            'idtopic' : idtopic,
                            'idrepondeur' : idrepondeur,
                            'reponse' : reponse,
                            'date' : date 
                        }
                        dic_forum['answer'] = dic_answer
                        forum_list.append(dic_forum)
                        
                    else:
                        topic = forum.topic
                        idUser = forum.idUser
                        forum_name = forum.forum
                        date = forum.date
                        dic_forum = {
                                'id' : forum.id,
                                'topic' : topic,
                                'idUser' : idUser,
                                'forum': forum_name,
                                'date' : date
                            }
                        forum_list.append(dic_forum)
            
        else:
            for forum in allforum:
                topic = forum.topic
                idUser = forum.idUser
                forum_name = forum.forum
                date = forum.date
                dic_forum = {
                                'id' : forum.id,
                                'topic' : topic,
                                'idUser' : idUser,
                                'forum': forum_name,
                                'date' : date
                            }
                forum_list.append(dic_forum)
        print(forum_list)    
        return render(request, 'forum.html',context={'forum_list': list(reversed(forum_list))})
    
    else:
        return render(request, 'login2.html')


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
            forum = request.POST['selectforum']
            if len(topic) != 0 and len(forum) != 0:
                date = datetime.now()
                
                addtopic = Forum(topic=topic, idUser=idUser, forum=forum, date=date)
                addtopic.save()
            else:
                pass
        else:
            pass
    
        return redirect('forumhome')
        
    else:
        render(request, 'login2.html')
            

def showtopic(request):
     if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            idtopic = request.POST['idtopic']
            topic  = Forum.objects.get(id=idtopic)
            list_answer = []
            try:
                answer = Answer.objects.filter(idtopic=idtopic) 
            except:
                pass
            topic = topic.topic
            
            return render(request, 'oneforum.html', context={'topic':topic, 'answer':answer})
        
    

def addanswer(request):
    '''
        Add the answer to DB
    '''
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            idrepondeur = logged_user_id
            idtopic = request.POST['idtopic']
            reponse = request.POST['reponse']
            date = datetime.now()
            addanswer = Answer(idtopic= int(idtopic), idrepondeur=idrepondeur, reponse=reponse, date=date)
            addanswer.save()
        else:
            pass
        
        return redirect('oneforum.html')
    else:
        return render(request, 'login2.html')


