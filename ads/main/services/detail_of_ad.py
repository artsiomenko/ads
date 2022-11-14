from main.models import Ad, Rubric
from main.services.search import SearchService


def detail_of_ad(request, rubric_name, ad_id):
    context = SearchService.__call__(request)
    context['ad'] = Ad.objects.get(pk=ad_id)
    context['rubric'] = Rubric.objects.get(name=rubric_name)
    return context
