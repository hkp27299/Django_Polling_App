from django.urls import path
from .views import signUp,signIn,createPoll,viewPoll

urlpatterns = [
    path('signup/', signUp,name='signup'),
    path('signin/', signIn,name='signin'),
    path('create/', createPoll,name='create'),
    path('view/', viewPoll,name='view'),



]
