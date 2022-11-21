from main.models import Ad


class AdsViewSetServices:
    @staticmethod
    def queryset_ads(pk):
        if not pk:
            return Ad.objects.all()
        return Ad.objects.filter(pk=pk)
