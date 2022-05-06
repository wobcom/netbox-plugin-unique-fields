from dcim.models import *
from extras.api.views import CustomFieldModelViewSet
from . import serializers
from ..filtersets import SIDFilterSet
from ..models import SID


class SIDViewSet(CustomFieldModelViewSet):
    queryset = SID.objects.all()
    serializer_class = serializers.SIDSerializer
    filterset_class = SIDFilterSet


