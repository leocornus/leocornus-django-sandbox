
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """the utility function for tostring"""
        return self.question_text

    def was_published_recently(self):
        """return true if it is publish less than one day"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """utility function for pretty print"""
        return self.choice_text
