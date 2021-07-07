from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import createPollForm

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
            login(request, user)
            if request.GET.get('next') != None:
                return redirect(request.GET.get('next'))
            else:
                return render(request,'home.html')

        else:
            message = 'Either password or username is wrong'

    template = 'signin.html'
    context = {'message':message}
    return render(request,template,context)

@login_required(login_url='signin')
def createPollView(request):
    form = createPollForm(request.POST or None)
    if form.is_valid():

        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        form = createPollForm()

    template = 'createPoll.html'
    context = {'form':form}
    return render(request,template,context)

@login_required(login_url='signin')
def viewPollView(request):
    template = 'viewPoll.html'
    context = {}
    return render(request,template,context)
