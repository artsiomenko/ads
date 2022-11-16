from main.models import Ad


class AdsQueryParamsServices:
    def queryset_ads(self, query_params):
        queryset = Ad.objects.all()
        queryset = self._filter_rubric(queryset, query_params)
        queryset = self._filter_author(queryset, query_params)
        queryset = self._filter_ad(queryset, query_params)
        return queryset

    @staticmethod
    def _filter_rubric(queryset, query_params):
        rubric_id = query_params.get('rubric')
        if rubric_id is not None:
            queryset = queryset.filter(rubric__id=rubric_id)
        return queryset

    @staticmethod
    def _filter_author(queryset, query_params):
        author_id = query_params.get('author')
        if author_id is not None:
            queryset = queryset.filter(author__id=author_id)
        return queryset

    @staticmethod
    def _filter_ad(queryset, query_params):
        ad_id = query_params.get('ad')
        if ad_id is not None:
            queryset = queryset.filter(id=ad_id)
        return queryset
