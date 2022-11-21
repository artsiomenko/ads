from main.models import Ad


class AdsViewSetServices:
    def queryset_ads(self, pk):
        if not pk:
            return Ad.objects.all()
        return Ad.objects.filter(pk=pk)
