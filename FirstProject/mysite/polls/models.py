from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Publish Date')


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    Num_of_votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
