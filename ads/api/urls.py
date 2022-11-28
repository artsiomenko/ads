from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *
from django.urls import path, include
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'ads', AdsViewSet, basename='ads')
# router.register(r'v1/ads', AdsListViewSet, basename='ads-list')

urlpatterns = [
    path('', include((router.urls, 'ads'))),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/ads/', AdsListViewSet.as_view(), name='ads-list'),
    path('v1/ads/<int:pk>/', AdDetail.as_view(), name='ad-detail'),
]
