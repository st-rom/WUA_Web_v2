from django.contrib import admin
from django.urls import path, include
from .views import analytics_graph, analytics_map, analytics_other

urlpatterns = [
    path('graph/', analytics_graph, name='analytics_graph'),
    path('map/', analytics_map, name='analytics_map'),
    path('other/', analytics_other, name='analytics_other'),
    # path('/', include('market.urls')),
]