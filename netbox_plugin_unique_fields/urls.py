from django.urls import path

from . import views

app_name = "netbox_plugin_unique_fields"

urlpatterns = [
    # Overlay Networks
    path('sids/add', views.SIDEditView.as_view(), name='sid_add'),
    path('sids/<int:pk>/delete', views.SIDDeleteView.as_view(),
         name='sid_delete'),
]
