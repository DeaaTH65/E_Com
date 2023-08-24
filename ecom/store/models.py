from django.db import models
import datetime


# categories of product
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
# customers



# product


# order