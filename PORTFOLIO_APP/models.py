from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    subject = models.CharField(max_length = 1000)
    message = models.CharField(max_length = 2500)
    date_time = models.DateTimeField()
    
    def __str__(self):
        return self.name