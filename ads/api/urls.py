from django.urls import path, include
from rest_framework import routers
from .views import AdsListAPIView, RubricViewSet

app_name = 'api'

##router = routers.DefaultRouter()
# router.register(r'^ads/', AdsListAPIView.as_view(), basename='ads-list')
# router.register(r'rubric', RubricViewSet)

urlpatterns = [
    path(r'api/ads/', AdsListAPIView.as_view(), name='ads-list'),
    # path('api/', include((router.urls, 'ads'))),
]
