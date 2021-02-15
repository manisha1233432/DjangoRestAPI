from django.db import models

class Usermodel(models.Model):
    id = models.CharField(max_length = 100, primary_key = True)
    real_name = models.CharField(max_length = 100)
    tz = models.CharField(max_length = 100)
     
class ActivityPeriod(models.Model):
    ActivityId = models.IntegerField(primary_key = True)
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now =False)
    id = models.ForeignKey(Usermodel,related_name = "Activity", on_delete = models.CASCADE )

