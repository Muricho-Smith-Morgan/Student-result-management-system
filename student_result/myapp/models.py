from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mark(models.Model):
    id = models.CharField(max_length= 20, primary_key=True)
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    mark = models.CharField(max_length=50)
    
    def __str__(self):
        return 'Name: {},Id: {}'.format(self.name,self.id)