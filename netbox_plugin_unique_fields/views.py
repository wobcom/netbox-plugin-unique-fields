
from netbox.views import generic
from .forms import *
from .models import SID


class SIDEditView(generic.ObjectEditView):
    model_form = SIDForm
    queryset = SID.objects.all()
    template_name = 'netbox_plugin_unique_fields/object_edit_singleton.html'


class SIDDeleteView(generic.ObjectDeleteView):
    queryset = SID.objects.all()
