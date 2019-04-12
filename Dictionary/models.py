import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Word (models.Model):
    word_text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word_text


class Desc(models.Model):
    # creates the one to many relation to word
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    # details of each individual desc
    desc_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.desc_text
