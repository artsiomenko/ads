from main.models import Ad, Rubric
from main.services.ads_and_rubric import ads_and_rubrics


def detail_of_ad_in_user_profile(request, rubric_name, ad_id):
    context = ads_and_rubrics()
    ad = Ad.objects.get(pk=ad_id)
    context['ad'] = ad
    context['rubric'] = Rubric.objects.get(name=rubric_name)
    return context