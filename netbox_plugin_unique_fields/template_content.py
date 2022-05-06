from extras.plugins import PluginTemplateExtension


class DeviceSID(PluginTemplateExtension):
    model = 'dcim.device'

    def right_page(self):
        return self.render('netbox_plugin_unique_fields/inc/device_sid.html')


template_extensions = [
    DeviceSID,
]
