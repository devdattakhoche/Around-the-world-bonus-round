from django.db import models

# Create your models here.

class Question(models.Model):
    Question = models.CharField(max_length = 30)
    Option_1 = models.CharField(max_length = 30)
    Option_2 = models.CharField(max_length = 30)
    Option_3 = models.CharField(max_length = 30)
    Option_4 = models.CharField(max_length = 30)
    
    def __str__(self):
        x = str(self.id)
        return x
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Quesiton'
        verbose_name_plural = 'Quesiton'

class Answer(models.Model):
    Question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    Ans = models.CharField(max_length = 30 ) 

    def __str__(self):
        x = str(self.Question_id)
        return x
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
