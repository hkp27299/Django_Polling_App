from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import createPollForm
from .models import createPoll

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
        obj.options = dict((x.strip(),0) for x in obj.options.split(','))
        print(obj.options)
        obj.save()

        form = createPollForm()

    template = 'createPoll.html'
    context = {'form':form}
    return render(request,template,context)

@login_required(login_url='signin')
def viewPollView(request):
    obj = createPoll.objects.all()
    template = 'viewPoll.html'
    context = {'obj':obj}
    return render(request,template,context)

@login_required(login_url='signin')
def vote(request,title,selectedoption):
    obj = createPoll.objects.get(title=title)
    dict = obj.options
    dict.update({selectedoption: obj.options[selectedoption]+1})
    obj.save()
    return redirect('view')
