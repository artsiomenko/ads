from django.db.models import Q

from main.models import Ad


class AdsFilterServices:
    def queryset_ads(self, query_params):
        queryset = Ad.objects.all()
        queryset = self._filter_price(queryset, query_params)
        queryset = self._filter_keyword(queryset, query_params)
        return queryset

    @staticmethod
    def _filter_price(queryset, query_params):
        ad_price = query_params.get('price')
        if ad_price is not None:
            queryset = queryset.filter(price__lte=ad_price)
        return queryset

    @staticmethod
    def _filter_keyword(queryset, query_params):
        keyword = query_params.get('keyword')
        if keyword is not None:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))
        return queryset
