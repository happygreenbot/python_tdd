from django.db import models

# Create your models here.
class List(models.Model):
    pass

class Item(models.Model):
    text = models.CharField(max_length = 30, default = '') 
    list = models.ForeignKey(List, default = None)


 