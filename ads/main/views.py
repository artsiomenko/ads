from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .models import Ad, Rubric
from .services.ads_and_rubric import ads_and_rubrics
from .services.detail_of_ad import detail_of_ad
from .services.detail_of_ad_in_user_profile import detail_of_ad_in_user_profile
from .services.page_division_by_rubric import page_division_by_rubric
from .services.search import SearchService
from .services.user_create_ad import user_create_ad
from .services.user_profile_page import user_profile_page


def index(request):
    return render(request, 'main/index.html', SearchService.__call__(request))


class BBLoginView(LoginView):
    template_name = 'main/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


@login_required
def profile(request):
    return render(request, 'main/profile.html', user_profile_page(request))


def by_rubric(request, rubric_name):
    return render(request, 'main/by_rubric.html', page_division_by_rubric(request, rubric_name))


def detail(request, rubric_name, ad_id):
    return render(request, 'main/detail.html', detail_of_ad(request, rubric_name, ad_id))


def profile_ad_detail(request, rubric_name, ad_id):
    return render(request, 'main/profile_ad_detail.html', detail_of_ad_in_user_profile(request, rubric_name, ad_id))


@login_required
def profile_new_ad(request):
    return render(request, 'main/profile_new_ad.html', user_create_ad(request))
