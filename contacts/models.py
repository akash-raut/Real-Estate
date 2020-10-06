from django.db import models
from datetime import datetime


class Contact(models.Model):
    ''' Contains data fields for Contact table '''
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.CharField(max_length=200, blank=True)
    contact_date = models.DateTimeField(default=datetime.now(), blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contact'

