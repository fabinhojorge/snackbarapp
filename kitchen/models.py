from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Ingredient(models.Model):
    name = models.CharField("Name", max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # measure_metric = # Will be a foreignKey to a list of options
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


# class Promotion:
#
#     def cheese_promotion(self):
#         """"""
#         ing_cheese = Ingredient.objects.get(name="Cheese")
#         cheese_promotion_price = ing_cheese.price
#         try:
#             quantity = self.ings.filter(ingredient=ing_cheese).get().amount
#         except ObjectDoesNotExist:
#             quantity = 0
#
#         discount_amount = cheese_promotion_price * (quantity//3)
#
#         return float(discount_amount)
#
#     def get_discount_promotion(self):
#         discount_amount = 0
#         for p in self.promotion_list:
#             discount_amount += p()
#         return discount_amount


class Product(models.Model):
    name = models.CharField("Product Name", max_length=150, blank=True)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField(Ingredient, through='ProductIngredient')

    def __str__(self):
        return "Product {0:05d} {1} ".format(self.id, self.name)


    def get_product_price(self):
        ings = self.productingredient_set.all()
        price_ings = sum([i.get_ingredient_price() for i in ings])

        discounts = 0
        # promotion = self.Promotion(ings)
        # discounts += promotion.get_discount_promotion()
        print("name: {0} price: {1}".format(self.name, price_ings))
        final_price = price_ings - discounts
        return final_price


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField("Amount", max_digits=2, decimal_places=0)

    def __str__(self):
        return "{0} - {1}".format(self.product, self.ingredient)

    def get_ingredient_price(self):
        return float(self.amount) * float(self.ingredient.price)
