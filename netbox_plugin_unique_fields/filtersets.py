import django_filters
from django.db.models import Q

from netbox.filtersets import ChangeLoggedModelFilterSet
from netbox_plugin_unique_fields.models import SID


class SIDFilterSet(ChangeLoggedModelFilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )



    class Meta:
        model = SID
        fields = ['id', 'sid']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(sid=value) |
            Q(id=value)
        )
