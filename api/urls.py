from django.template.defaulttags import url
from django.urls import path

from .views import TableViewSet

urlpatterns = [
    path('table_list', TableViewSet.as_view({'get': 'list'})),
    # path('track_list/?sort=get_parameter_name/', TableViewSet.as_view({'get': 'sort_list'})),
]
