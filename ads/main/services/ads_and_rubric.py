from main.models import Rubric, Ad


def ads_and_rubrics():
    rubrics = Rubric.objects.all()
    ads = Ad.objects.all()
    context = {'ads': ads, 'rubrics': rubrics}
    return context
