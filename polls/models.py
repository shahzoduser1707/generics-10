from django.db import models
from datetime import datetime
# Create your models here.



class StreetModel(models.Model):
    name = models.CharField(max_length=300,default='')
    created_at = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=200,default='')
    desc = models.TextField(default='write!')


    class Meta:
        db_table = 'StreetModel'
    def __str__(self) -> str:
        return self.name