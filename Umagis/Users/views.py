from django.shortcuts import render, HttpResponse
from Users.models import Users
from . import maps
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
        svg = maps.svg
        new_svg = []
        #print(svg[-1]['shape'])     
        for svg in svg:
            svg = {
                'id' : svg['id'],
                'shape' : svg['shape'].replace(' ',',')
            }
            new_svg.append(svg)
            
        if request.method == 'POST':
            print(name)
            return render(request, 'thestudents.html', context={'svg':new_svg})
            
            
        else:
            return render(request, 'thestudents.html', context={'svg':new_svg})
    
    else:
        return render(request, 'student.html')
        
def contry(request):
    '''
        One contry selected
    '''
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Users.objects.get(id=logged_user_id)
        
        return render(request, 'student.html')


def student1(request):
    '''
        The information of student
    '''
    me = request.POST['name']
    return HttpResponse(me)