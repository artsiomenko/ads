from .views import *
from django.urls import path, include
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'ads', AdsViewSet, basename='ads')

urlpatterns = [
    path('', include((router.urls, 'ads'))),
]
