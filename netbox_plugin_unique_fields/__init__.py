from extras.plugins import PluginConfig


class PluginUniqueFields(PluginConfig):
    name = "netbox_plugin_unique_fields"
    verbose_name = "Unique Fields Plugin"
    description = ""
    version = "0.0.0"
    author = "Johann Wagner"
    author_mail = "johann.wagner@wobcom.de"
    base_url = "unique_fields"


config = PluginUniqueFields
