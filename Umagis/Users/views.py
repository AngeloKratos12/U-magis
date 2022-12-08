from django.shortcuts import render, HttpResponse
from Users.models import Users
# Create your views here.

#def login(request):

def student(request):
    '''
        The information of student
    '''
    name = 'angelo Kratos miharimanana'
    vide='None'
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        if request.method == 'POST':
            print(name)
            return render(request, 'student.html', context={'name':name})
            
            
        else:
            return render(request, 'student.html', context={'name':vide})
    
    else:
        return render(request, 'login.html')
        


def student1(request):
    '''
        The information of student
    '''
    me = request.POST['name']
    return HttpResponse(me)