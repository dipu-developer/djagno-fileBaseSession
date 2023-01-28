from django.shortcuts import render


def setsession(request):
    request.session['name'] = 'Deepak' 
    return render(request,'setsession.html')  

def getsession(request):
    name = request.session['name']          
    return render(request,'getsession.html',{'name':name})

def delsession(request):
    if 'name'in request.session:
        request.session.flush()             
        request.session.clear_expired()
        return render(request,'delsession.html')
    return render(request,'delsession.html',{'message': 'User already delete'})
    
