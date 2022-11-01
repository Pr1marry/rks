from django.template.defaulttags import url
from django.urls import path

from .views import TableViewSet

urlpatterns = [
    path('table_list', TableViewSet.as_view({'get': 'list'})),
    # path('track_list/<int:pk>/', TrackViewSet.as_view({'get': 'get_list'})),
]
