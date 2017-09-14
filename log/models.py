from django.db import models

# Create your models here.
class Log(models.Model):
    name=models.CharField(max_length=40)
    date=models.DateField(max_length=50)
    description=models.CharField(max_length=400)
    time=models.TimeField(max_length=50)

    def __str__(self):
        return str(self.name)

