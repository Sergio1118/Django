from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsViews.as_view(), name='lista-productos'),  # Para listar y crear 
    path('producto/<int:pk>/', views.ProductsViews.as_view(), name='producto'),  # Para detalles, 
]
