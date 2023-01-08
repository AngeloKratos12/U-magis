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
        #print(allforum)
        forum_list = []
        answer_list = []
        
        for forum in allforum:
            topic = forum.topic
            idUser = forum.idUser
            forum_name = forum.forum
            date = forum.date
            answer_topic = Answer.objects.filter(idtopic=forum.id)
            nbr_answer = len(answer_topic) 
            dic_forum = {
                        'id' : forum.id,
                        'topic' : topic,
                        'idUser' : idUser,
                        'forum': forum_name,
                        'date' : date,
                        'nbr_answer': nbr_answer
                        }
            forum_list.append(dic_forum)
        
        print(len(forum_list))    
        return render(request, 'forum.html',context={'forum_list': list(reversed(forum_list)), 'nbr_forum':len(forum_list)})
    
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
            #print(len(request.POST['reponse']))
            try:
                #if request.POST['reponse']:
                    idrepondeur = logged_user_id
                    idtopic = request.POST['idtopic']
                    reponse = request.POST['reponse']
                    date = datetime.now()
                    addanswer = Answer(idtopic= int(idtopic), idrepondeur=idrepondeur, reponse=reponse, date=date)
                    addanswer.save()
                    
                    
            except:
                pass
            
            answer = Answer.objects.filter(idtopic=idtopic)
            for ans in answer:
                        #print(ans.idrepondeur)
                user_answered = Users.objects.get(id=ans.idrepondeur)
                            #print(user_answered.user_name)
                result = {
                                'user':user_answered.user_name,
                                'answer':ans.reponse,
                                'date':ans.date,
                                'classe':user_answered.classe,
                                'contacte':user_answered.contacte,
                            }
                            #print(result)
                list_answer.append(result)
                        #print(list_answer)
                        
                
            topic = topic.topic
            
        return render(request, 'oneforum.html', context={'topic':topic, 'answer':list_answer,'idtopic':idtopic})
        
    



