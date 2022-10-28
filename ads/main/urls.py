from django.urls import path

from .views import index, about, BBLoginView, profile, BBLogoutView, RegisterDoneView, \
    RegisterUserView, user_activate, by_rubric, detail, profile_ad_detail, profile_new_ad

app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/add/create/', profile_new_ad, name='profile_new_ad'),
    path('accounts/profile/<str:rubric_name>/<int:ad_id>/', profile_ad_detail, name='profile_ad_detail'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:rubric_name>/<int:ad_id>/show/', detail, name='detail'),  # Transport/1/show
    path('<str:rubric_name>/', by_rubric, name='by_rubric'),  # Transport
    path('about/', about, name='about'),
    path('', index, name='index')
]
