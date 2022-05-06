from netbox.api import OrderedDefaultRouter
from . import views


router = OrderedDefaultRouter()

# Sites
router.register('sids', views.SIDViewSet)

app_name = 'netbox_plugin_unique_fields-api'
urlpatterns = router.urls
