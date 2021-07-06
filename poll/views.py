from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def signUp(request):
    obj = request.POST or None
    if obj is not None:
        user = User.objects.create_user(obj['fname'], obj['email'],obj['psw'])
        user.last_name = obj['lname']
        user.first_name = obj['fname']
        user.save()
    template = 'signup.html'
    context = {}
    return render(request,template,context)

def signIn(request):
    obj = request.POST or False
    message = None
    if obj:
        user = authenticate(username = obj['fname'], password = obj['psw'])
        if user is not None:
            message = "user successfully signed in"
            return render(request,'home.html')
        else:
            message = 'Either password or username is wrong'

    template = 'signin.html'
    context = {'message':message}
    return render(request,template,context)

def createPoll(request):
    template = 'createPoll.html'
    context = {}
    return render(request,template,context)

def viewPoll(request):
    template = 'viewPoll.html'
    context = {}
    return render(request,template,context)
