from django.db import models

class data(models.Model):
   search = models.TextField(max_length=50)
   title = models.TextField(max_length=50)
   pron = models.TextField(max_length=50)
   type = models.TextField(max_length=20)
   # info = models.FileField()
