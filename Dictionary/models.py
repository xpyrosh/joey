import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class UDict(models.Model):
    # word can have multiple descriptions
    word_text = models.CharField(max_length=100)
    desc_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.word_text
