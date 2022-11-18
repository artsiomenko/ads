from .views import AdsListFilterViewSet, AdViewSet, RubricViewSet
from django.urls import path, include
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'ads', AdViewSet)
router.register(r'rubric', RubricViewSet)

urlpatterns = [
    path('', AdsListFilterViewSet.as_view(), name='ads-filters'),
    path('', include((router.urls, 'ads'))),
]
