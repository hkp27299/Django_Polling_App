from django.urls import path
from .views import signUp,signIn,createPollView,viewPollView,vote

urlpatterns = [
    path('signup/', signUp,name='signup'),
    path('signin/', signIn,name='signin'),
    path('create/', createPollView,name='create'),
    path('view/', viewPollView,name='view'),
    path('vote/<str:title>/<str:selectedoption>', vote, name='vote'),
]
