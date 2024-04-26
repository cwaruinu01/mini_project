from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from members.models import users
from django.views.decorators.csrf import csrf_exempt


def members(request):
    return HttpResponse("Hello world!")


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template)


def dashboard(request):
    mydata = users.objects.all()  # Retrieve all user data
    context = {'mydata': mydata}  # Pass data to the template context
    return render(request, 'dashboard.html', context)


@csrf_exempt
def adduser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        myuser = {'name': name, 'email': email, 'age': age}
        print(myuser)

        object = users(name=name, email=email, age=age)
        object.save()

        mydata = users.objects.all()
        context = {'mydata': mydata}
        return render(request, 'dashboard.html', context)
    else:
        return HttpResponse("GET request received. Use POST method to add a user.")


def deleteuser(request, id):
    deleteuser = users.objects.get(id=id)
    deleteuser.delete()
    return redirect('/dashboard')


def edituser(request,id):
    data = users.objects.get(id=id)
    context = {'data': data}
    return render(request, 'edituser.html', context)


def updateuser(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        edit = users.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.save()

    data = users.objects.all()
    context = {'data': data}
    return render(request, 'dashboard.html', context)
