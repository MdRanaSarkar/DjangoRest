from django.db import models

# Create your models here.


class Task(models.Model):
    taskname=models.CharField(max_length=200)
    handler=models.CharField(max_length=200)


    def __str__(self):
        return  self.taskname