from django.db import models


class Questions(models.Model):
    question_txt = models.CharField(max_length=280)
    pub_date = models.DateTimeField('Date Published')

    def _str_(self):
        return self.question_txt


class Choicing(models.Model):
    questions = models.ForeignKey(to = 'Questions',on_delete = models.CASCADE)
    choice_txt = models.CharField(max_length=280)
    vote_to = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_txt






# Create your models here.
