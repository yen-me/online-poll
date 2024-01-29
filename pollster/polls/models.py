from django.db import models

# Create your models here.


class Question(models.Model):
    # ID will be created automatically
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Display question_text instead of QuestionObject:
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # CASCADE: When question is deleted, all of the choices under the question also be deleted.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
