from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from api.account.views import UserViewset

app_name = 'account'

urlpatterns = [
    path('jwt/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserViewset.as_view({'get': 'list', 'post': 'create'}))
]
