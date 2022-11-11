from django.db.models import Q
from main.forms import SearchForm


def search(request, ads):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(content__icontains=keyword)
        ads = ads.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword': keyword})
    return ads, form
