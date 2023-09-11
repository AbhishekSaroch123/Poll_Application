from django.db import models

# we have two models in our application
# fields in our models

class Question(models.Model):
    # models.type of field(length of question)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    # related question is deleted all choices deletd
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)