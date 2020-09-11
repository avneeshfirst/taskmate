from django.db import models
from django.contrib.auth.models import User

class Tasklist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    task = models.CharField(max_length=50)
    jobStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.task + '--' + str(self.jobStatus)
    