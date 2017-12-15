# Create your models here.
"""
Definition of models.
"""

from django.db import models

# Each model extends models.Model
class Publisher(models.Model): 
    # Simple definition of string field
    name = models.CharField(max_length=30) 
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    # Simple definition of URL field
    website = models.URLField() 

class Book(models.Model):
    title = models.CharField(max_length=100)
     # Defines a foreign key to Publisher
    publisher = models.ForeignKey(Publisher)
     # Date field definition
    publication_date = models.DateField()
