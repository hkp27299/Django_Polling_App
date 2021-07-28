from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import signUp,signIn,createPollView,viewPollView,vote
from django.contrib import admin
urlpatterns = [
    path('signup/', signUp,name='signup'),
    path('signin/', signIn,name='signin'),
    path('create/', createPollView,name='create'),
    path('view/', viewPollView,name='view'),
    path('vote/<str:title>/<str:selectedoption>', vote, name='vote'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
