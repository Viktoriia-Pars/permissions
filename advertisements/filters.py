from django_filters import rest_framework as filters
from django_filters import DateTimeFromToRangeFilter, ChoiceFilter, DateFromToRangeFilter

from .models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()


    class Meta:
        model = Advertisement
        fields = ['created_at','status', 'creator']
