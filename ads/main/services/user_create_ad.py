from main.forms import AdForm
from main.models import Ad, Rubric
from django.shortcuts import render


def user_create_ad(request):
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
    return context
