import json
from django.http import HttpResponse, JsonResponse
from .models import Products
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request, pk=None):
    """
    Default endpoint for Products application.
    """

    if request.method == "GET":
        if pk:
            products = Products.objects.get(id=pk)
            return JsonResponse(data={"message": "ok",
                                      "id": products.id,
                                      "name": products.product_name,
                                      "price": products.product_price,
                                      "stock": products.product_stock})
        else:
            products = list(Products.objects.all().values("id",
                                                          "product_name",
                                                          "product_price",
                                                          "product_type",
                                                          "product_stock"))

            return JsonResponse(data={"message": "ok", "products": products})


        # products_list = Products.objects.all()
        # template = loader.get_template('products/index.html')
        # message = {"products_list": products_list}
        # return HttpResponse(template.render(message, request))

    if request.method == 'POST':
        
        body = request.body.decode('utf-8')
        request_body = json.loads(body)   
        
        product = Products.objects.create(
            product_name = request_body['name'],
            product_price = request_body['price'],
            product_type = request_body['type'],
            product_stock = request_body['stock']
        )
        
        return JsonResponse(data={'message': 'OK',
                                  'name': product.product_name,
                                  'price': product.product_price})

    if request.method == "DELETE":
        if pk:
            Products.objects.filter(id=pk).delete()
            return JsonResponse(data={"message": "Product with id = " + str(pk) + " deleted"})

    return HttpResponse("Method not allowed", status=405)