import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class UDict(models.Model):
    word = models.CharField(100)
    word.unique = True
    definitions = [ Desc ]

    def __str__(self):
        return self.word


class Desc(models.Model):
    desc_text = models.TextField()
    date_posted = models.DateTimeField('Date Posted')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.desc_text
