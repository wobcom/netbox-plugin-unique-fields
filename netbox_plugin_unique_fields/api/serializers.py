from rest_framework import serializers

from dcim.api.nested_serializers import NestedDeviceSerializer
from dcim.models import *
from netbox.api.serializers import CustomFieldModelSerializer
from netbox_plugin_unique_fields.models import SID


class SIDSerializer(CustomFieldModelSerializer):
    device = NestedDeviceSerializer()

    class Meta:
        model = SID
        fields = [
            'id', 'device', 'sid', 'created', 'last_updated',
        ]
