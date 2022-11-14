from main.models import Rubric
from main.services.search import SearchService


def page_division_by_rubric(request, rubric_name):
    context = SearchService.__call__(request)
    context['ads'] = context['ads'].filter(rubric=Rubric.objects.get(name=rubric_name))
    context['rubric'] = Rubric.objects.get(name=rubric_name)
    return context
