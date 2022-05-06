from netbox_plugin_unique_fields.models import SID
from utilities.forms import BootstrapMixin, DynamicModelChoiceField
from django import forms
from dcim.models import Device

__all__ = [
    'SIDForm',
]


class SIDForm(BootstrapMixin, forms.ModelForm):

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
    )

    class Meta:
        model = SID
        fields = ('device', 'sid')

