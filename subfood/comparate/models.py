from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=200)

<<<<<<< Updated upstream
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
=======
class Products(models.Model):
>>>>>>> Stashed changes
    nutriscore = models.CharField(max_length=1)
    categories = models.ManyToManyField(Categories)
    vegg = models.BooleanField()
    vegan = models.BooleanField()
    fat = models.FloatField(max_length=10)
    sugar = models.FloatField(max_length=10)
    salt = models.FloatField(max_length=10)
    origin = models.CharField(max_length=200)

<<<<<<< Updated upstream
    def __str__(self):
        return self.name

class Favorite(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.users
=======
class Favorite(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
>>>>>>> Stashed changes
