from django.db import models


class Receipe(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=500)
    method = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


