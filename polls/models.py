from django.db import models
from django.utils import timezone
from datetime import timedelta


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def choice_win(self):
        '''
        :return: winner choice
        '''
        return self.choices.all().order_by('votes').last()

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def is_win(self):
        '''
        :return: True if this choice is win
        '''
        return self.votes >= self.question.choice_win().votes

    def __str__(self):
        return self.choice_text
