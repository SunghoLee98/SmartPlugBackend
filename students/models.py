from django.db import models


class Eproduct(models.Model):
    s_no = models.CharField(max_length=100)
    s_wat = models.IntegerField(default=0)
    
    def __str__(self):
        return self.s_no
# Create your models here.
