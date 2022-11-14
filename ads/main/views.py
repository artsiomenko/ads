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
from .services.search import SearchService
from .services.user_create_ad import user_create_ad


def index(request):
    context = SearchService.__call__(request)
    return render(request, 'main/index.html', context)


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
    rubrics, ads = Rubric.objects.all(), Ad.objects.filter(author=request.user.pk)
    context = {'ads': ads, 'rubrics': rubrics}
    return render(request, 'main/profile.html', context)


def by_rubric(request, rubric_name):
    current_rubric = Rubric.objects.get(name=rubric_name)
    ads = Ad.objects.filter(rubric=current_rubric)
    rubrics = Rubric.objects.all()
    ads, form = search(request, ads)
    context = {'ads': ads, 'rubrics': rubrics, 'current_rubric': current_rubric, 'form': form}
    return render(request, 'main/by_rubric.html', context)


def detail(request, rubric_name, ad_id):
    rubrics = Rubric.objects.all()
    rubric = Rubric.objects.get(name=rubric_name)
    ad = Ad.objects.get(pk=ad_id)
    ads, form = search(request, Ad.objects.all())
    context = {'ad': ad, 'rubrics': rubrics, 'rubric': rubric, 'form': form}
    return render(request, 'main/detail.html', context)


def profile_ad_detail(request, rubric_name, ad_id):
    rubrics = Rubric.objects.all()
    rubric = Rubric.objects.get(name=rubric_name)
    ad = Ad.objects.get(pk=ad_id)
    context = {'ad': ad, 'rubrics': rubrics, 'rubric': rubric}
    return render(request, 'main/profile_ad_detail.html', context)


@login_required
def profile_new_ad(request):
    rubrics = Rubric.objects.all()
    context = user_create_ad(request, rubrics)
    return render(request, 'main/profile_new_ad.html', context)
