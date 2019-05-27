from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    imgurl = models.CharField(max_length=500)
    cost = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name