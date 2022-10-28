from django.urls import path

from .views import index, BBLoginView, profile, BBLogoutView, RegisterDoneView, \
    RegisterUserView, user_activate, by_rubric, detail, profile_ad_detail, profile_new_ad, about

app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/ads/create/', profile_new_ad, name='profile_new_ad'),
    path('accounts/profile/ads/<str:rubric_name>/<int:ad_id>/show/', profile_ad_detail, name='profile_ad_detail'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path(r'rubrics/<str:rubric_name>/<int:ad_id>/show/', detail, name='detail'),  # rubrics/Transport/1/show
    path(r'rubrics/<str:rubric_name>/', by_rubric, name='by_rubric'),  # rubrics/Transport
    path('about/', about, name='about'),
    path('', index, name='index')
]
