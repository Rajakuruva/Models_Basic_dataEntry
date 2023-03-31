from django.db import models

# Create your models here.

class Games(models.Model):
    Gname=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Gname

class Player(models.Model):
    Gname=models.ForeignKey(Games,on_delete=models.CASCADE)
    Pname=models.CharField(max_length=100,primary_key=True)
    Page=models.IntegerField()
    Purl=models.URLField()
    def __str__(self):
        return self.Pname
