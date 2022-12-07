from django.shortcuts import render, HttpResponse

# Create your views here.

#def login(request):

def student(request):
    '''
        The information of student
    '''
    name = 'Angelomiharimanana'
    return render(request, 'student.html', context={'name':name})


def student1(request):
    '''
        The information of student
    '''
    me = request.POST['name']
    return HttpResponse(me)