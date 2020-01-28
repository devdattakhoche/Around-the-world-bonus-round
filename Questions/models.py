from django.db import models

# Create your models here.


class Question(models.Model):
    id = models.IntegerField(primary_key=True , unique=True, null=False, blank=False)
    Question = models.CharField(max_length=300)
    Option_1 = models.CharField(max_length=60)
    Option_2 = models.CharField(max_length=60)
    Option_3 = models.CharField(max_length=60)
    Option_4 = models.CharField(max_length=60)

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
    Ans = models.CharField(max_length=60)

    def __str__(self):
        x = str(self.Question_id)
        return x

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
