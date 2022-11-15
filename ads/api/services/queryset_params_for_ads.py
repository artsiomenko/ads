from main.models import Ad


def queryset_ads(self):
    queryset = Ad.objects.all()
    rubric_id = self.request.query_params.get('rubric_id')
    if rubric_id is not None:
        queryset = queryset.filter(rubric__id=rubric_id)

    author_id = self.request.query_params.get('author_id')
    if author_id is not None:
        queryset = queryset.filter(author__id=author_id)

    ad_id = self.request.query_params.get('id')
    if ad_id is not None:
        queryset = queryset.filter(id=ad_id)
    return queryset
