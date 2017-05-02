from django.db import models
from django.utils import timezone

class Question (models.Model):
    question_text=models.CharField(max_length=200);
    pub_date=models.DateField("ciaoscemo")
    def __str__(self):
        return self.question_text;
    def waspubliscied今月(self):
        return self.pub_date.month==timezone.now().month;

class Choice (models.Model):
    question=models.ForeignKey(Question)
    choiche_text=models.CharField(max_length=200);
    votes=models.IntegerField(default=0);
    def __str__(self):
        return self.choiche_text;