from django.shortcuts import render
from .models import userModel

def signUp(request):
    template = 'signup.html'
    context = {}
    return render(request,template,context)
