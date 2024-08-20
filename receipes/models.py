from django.db import models
from django.contrib.postgres.fields import ArrayField

class Receipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    ingredients = models.TextField(max_length=500)
    method = models.TextField(max_length=2000)
    categories = ArrayField( 
           models.CharField(max_length=30, blank=True), default=list)
           
    

    def __str__(self):
        return self.title


