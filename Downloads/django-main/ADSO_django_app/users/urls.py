from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_user, name='create'),
    path('users_list/',views.users_list, name='users_list'),
    path('user_detail/<str:name>/', views.user_detail, name='user_detail'),
    path('update_user/<str:name>/', views.update_user, name='update_user'),
    path('delete_user/<str:name>/', views.delete_user, name='delete_user'),
]


