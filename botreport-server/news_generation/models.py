from apscheduler.schedulers.background import BackgroundScheduler
from django.db import models

# Create your models here.


class LiveNews(models.Model):
    text = models.TextField()
    data = models.TextField()

    def __str__(self):
        return self.text

