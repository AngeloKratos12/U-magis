from django.shortcuts import render
from Users.models import Users
from datetime import datetime
from . import models

# Create your views here.
def home(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        list_question = []
        question = models.Question.objects.all()
        for quest in question:
            user = Users.objects.get(id=quest.idUser)
            dic_question = {
                'question' : quest.question,
                'about' : quest.about,
                'detail' : quest.detail,
                'user' : user.user_name,
                'user_class' : user.classe,
                'date' : quest.date,
            }
            list_question.append(dic_question)
        
        return render(request, 'studyoverflow.html', context={'questions' : list(reversed(list_question))})
    else:
        return render(request, 'login2.html')



def ask(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        
        if request.method == 'POST':
            question = request.POST['question']
            about = request.POST['about']
            detail = request.POST['detail']
            user = logged_user_id
            date = datetime.now()
            if len(question) != 0 and len(about) != 0 and len(detail) != 0:
                addquestion = models.Question(question=question, about=about, detail=detail, idUser=user, date=date )
                addquestion.save()
            else:
                pass
        
        return render(request, 'ask.html')
    else:
        return render(request, 'login2.html')
    