from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image_url = models.URLField()
    category = models.CharField(choices=[('computers', 'Computers'),
                                         ('house', 'House and Garden'),
                                         ('clothing', 'Clothing'),
                                         ('car', 'Car Products'),
                                         ('toys', 'Toys')], max_length=30, default=1)

    def __str__(self):
        return str(self.title)


class Cart(models.Model):
    username = models.CharField(max_length=40, unique=True)
    products = models.JSONField(null=True)

    def __str__(self):
        return self.username
