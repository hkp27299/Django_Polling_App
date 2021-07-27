from django.db import models
from django.conf import settings
from picklefield.fields import PickledObjectField
# Create your models here.
User = settings.AUTH_USER_MODEL

class createPoll(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length = 300, blank = False)
    options = PickledObjectField(editable = True)
