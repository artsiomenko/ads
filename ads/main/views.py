from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm, AdForm
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.core.signing import BadSignature
from .utilities import signer
from .models import Ad, Rubric


def index(request):
    ads = Ad.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    context = {'ads': ads, 'rubrics': rubrics}
    return render(request, 'main/index.html', context)


def about(request):
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics}
    return render(request, 'main/about.html', context)


class BBLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def profile(request):
    rubrics = Rubric.objects.all()
    ads = Ad.objects.filter(author=request.user.pk)
    context = {'ads': ads, 'rubrics': rubrics}
    return render(request, 'main/profile.html', context)


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(User, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html'
    else:
        template = 'main/activation_done.html '
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


def by_rubric(request, rubric_name):
    current_rubric = Rubric.objects.get(name=rubric_name)
    ads = Ad.objects.filter(rubric=current_rubric)
    rubrics = Rubric.objects.all()
    context = {'ads': ads, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'main/by_rubric.html', context)


def detail(request, rubric_name, ad_id):
    rubrics = Rubric.objects.all()
    rubric = Rubric.objects.get(name=rubric_name)
    ad = Ad.objects.get(pk=ad_id)
    context = {'ad': ad, 'rubrics': rubrics, 'rubric': rubric}
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
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            ads = Ad.objects.filter(author=request.user.pk)
            context = {'form': form, 'ads': ads, 'rubrics': rubrics}
            return render(request, 'main/profile.html', context)
    else:
        form = AdForm(initial={'author': request.user.pk})
        ads = Ad.objects.filter(author=request.user.pk)
        context = {'form': form, 'ads': ads, 'rubrics': rubrics}
    return render(request, 'main/profile_new_ad.html', context)


@login_required
def update(request, rubric_name, ad_id):
    rubrics = Rubric.objects.all()
    rubric = Rubric.objects.get(name=rubric_name)
    ad = Ad.objects.get(pk=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST, instanсe=ad)
        if form.is_valid():
            form.save()
            ads = Ad.objects.filter(author=request.user.pk)
            context = {'form': form, 'ads': ads, 'rubrics': rubrics}
            return render(request, 'main/profile.html', context)
    else:
        form = AdForm(instanсe=ad)
        ads = Ad.objects.filter(author=request.user.pk)
        context = {'form': form, 'ads': ads, 'rubrics': rubrics, 'rubric': rubric}
    return render(request, 'main/update.html', context)







