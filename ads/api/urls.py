from django.urls import path, include
from rest_framework import routers
from .views import AdsListViewSet, RubricViewSet

app_name = 'api'

# router = routers.SimpleRouter()
# router.register(r'ads', AdsViewSet)
# router.register(r'rubric', RubricViewSet)
# router.register(r'accounts/profile/ads', AdsViewSet)

urlpatterns = [
    path('api/ads/', AdsListViewSet.as_view(), name='ads-list')
    # path('api/', include((router.urls, 'ads'))),
]
