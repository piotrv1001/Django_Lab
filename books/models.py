from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year= models.IntegerField()
    create_time = models.DateTimeField('create time')
    last_edit_time = models.DateTimeField('last edit time')



