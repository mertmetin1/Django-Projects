from django.db import models



class Bot_Setting(models.Model):
    isRunning=models.BooleanField(default=False)
    CheckFrequency=models.IntegerField(default=1)
    CheckToDate=models.IntegerField(default=90)
    
    def __str__(self):
        return "isRunning: "+str(self.isRunning)