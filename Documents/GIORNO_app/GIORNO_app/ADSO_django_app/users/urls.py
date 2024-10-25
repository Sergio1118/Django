from . import views
from rest_framework_simplejwt import views as jwt_views
from django.urls import path


urlpatterns = [
    path('signUp/', views.SignUp.as_view(), name='signUp'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
