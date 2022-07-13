from django.db import models

class Members(models.Model):
    Name = models.CharField(max_length=255)
    Genre = models.CharField(max_length=255)
    Year = models.CharField(max_length=255)

    
