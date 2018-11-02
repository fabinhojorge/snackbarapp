from django.db import models


class Ingredient(models.Model):
    name = models.CharField("Name", max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # measure_metric = # Will be a foreignKey to a list of options
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Product Name", max_length=150, blank=True)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return "Product {0:05d} {1} ".format(self.id, self.name)
