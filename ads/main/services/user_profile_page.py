from main.services.ads_and_rubric import ads_and_rubrics


def user_profile_page(request):
    context = ads_and_rubrics()
    context['ads'] = context['ads'].filter(author=request.user.pk)
    return context
