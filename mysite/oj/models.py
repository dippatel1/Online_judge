from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models



import datetime

from django.db import models
from django.utils import timezone


class user(models.Model):
    user_id=models.CharField(max_length=200)
    user_name=models.CharField(max_length=1000)
    user_pass=models.CharField(max_length=10)
    def __str__(self):
        return self.user_id


class Question(models.Model):
    
    question_name = models.CharField(max_length=200)
    question_des=models.CharField(max_length=1000)
    question_diff=models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class TestCases(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    input_testcases = models.CharField(max_length=1000)
    otput_testcases = models.CharField(max_length=1000)
    def __str__(self):
        return self.input_testcases

class Submissions(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Submission_verdict=models.CharField(max_length=10,default="unsolved")
    submission_date = models.DateTimeField('date submitted')
    submitted_code=models.CharField(max_length=1000,default="")

