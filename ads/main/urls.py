from django.urls import path
from .views import index, BBLoginView, profile, BBLogoutView, RegisterDoneView, \
    RegisterUserView, by_rubric, detail, profile_ad_detail, profile_new_ad

app_name = 'main'

urlpatterns = [
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/ads/<str:rubric_name>/<int:ad_id>/', profile_ad_detail, name='profile_ad_detail'),
    path('accounts/profile/ads/', profile_new_ad, name='profile_new_ad'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path(r'<str:rubric_name>/<int:ad_id>/', detail, name='detail'),  # /Transport/1/
    path(r'<str:rubric_name>/', by_rubric, name='by_rubric'),  # /Transport
    path('', index, name='index')
]
