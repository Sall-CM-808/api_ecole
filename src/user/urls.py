from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from user import views
urlpatterns = [
    #Url qui permet l'authentification par token et qui permet d'obtenir un token
    path('tokenAuthentication',ObtainAuthToken.as_view(),name='obtain_token'),
    #URLS qui permettent l'authentification pour JWT(Json Web Token)
    path('token',TokenObtainPairView.as_view(),name='obtain_token'),
    path('token/refresh',TokenRefreshView.as_view(),name=('refresh_token')),
    path('token/verify',TokenVerifyView.as_view(), name='token_verify'),
    #URL pour la gestion des USERS
    path('create',views.UserCreateAPI.as_view(),name='user_create'),
]
