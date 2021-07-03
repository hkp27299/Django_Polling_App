from django.urls import path
from .views import signUp,signIn

urlpatterns = [
    path('signup/', signUp,name='signup'),
    path('signin/', signIn,name='signin'),

]
