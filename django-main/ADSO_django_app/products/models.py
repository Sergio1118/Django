from django.db import models


# Create your models here.
class Products(models.Model):
    """
    Products Model to manage type and info about products db.
    """
    product_name = models.CharField(max_length=100, null=False, verbose_name="Product Name")
    product_price = models.DecimalField(decimal_places=2, verbose_name="Product Price", max_digits=10)
    product_type = models.CharField(max_length=100, null=False, verbose_name="Product Type")
    product_stock = models.IntegerField(verbose_name="Product Stock")
