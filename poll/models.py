from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class createPoll(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length = 300, blank = False)
    options = models.CharField(max_length = 300)
