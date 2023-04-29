from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    text = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.name
