from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from members.models import users
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect


def members(request):
    return HttpResponse("Hello world!")


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template)

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())

@csrf_exempt
def adduser(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        myuser={'name':name,'email':email,'age':age}
        print(myuser)

        object=users(name=name,email=email,age=age)
        object.save()

        myuser=users.objects.all()
        context={'object':myuser}
        return render(request,'dashboard.html',context)