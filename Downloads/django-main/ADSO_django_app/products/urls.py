from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Lista-Protudos/', views.productviews.as_view(), name='Lista-Protudos'),
    path('<int:pk>/', views.index, name='index'),
]
