from .views import *
from django.urls import path, include
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
# router.register(r'ads', AdViewSet)
# router.register(r'rubric', RubricViewSet)
router.register(r'ads', AdsViewSetCRUD, basename='ads')

urlpatterns = [
    path('', AdsListFilterViewSet.as_view(), name='ads-filters'),
    path('', include((router.urls, 'ads'))),
]
