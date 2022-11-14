from django.db.models import Q
from main.forms import SearchForm
from main.models import Ad, Rubric


class SearchService:

    def __call__(self):
        ads, rubrics = Ad.objects.all(), Rubric.objects.all()
        if 'keyword' in self.GET:
            keyword = self.GET['keyword']
            q = Q(title__icontains=keyword) | Q(content__icontains=keyword)
            ads = ads.filter(q)
        else:
            keyword = ''
        form = SearchForm(initial={'keyword': keyword})
        context = {'ads': ads, 'rubrics': rubrics, 'form': form}
        return context
