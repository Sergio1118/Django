from  rest_framework import serializers
from .models import Products

class produt_serialiazar(serializers.ModelSerializer):
  
  class Meta:
    model=Products
    fields=['id',
            'product_name',
            'product_price',
            'product_type',
            'product_stock']