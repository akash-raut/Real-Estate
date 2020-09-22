from django.db import models
from datetime import datetime


class Realtor(models.Model):
    ''' Includes the information about Realtor '''
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    is_mvp = models.BooleanField(default=False)  # Seller of the month
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'realtor'

    def __str__(self):
        return self.name


