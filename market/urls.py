from django.contrib import admin
from django.urls import path, include
from .views import market_list, market_create, gen_detail

urlpatterns = [
    path('create/', market_create, name='market_create'),
    path('list/', market_list, name='market_list'),
    path('details/<int:pk>/', gen_detail, name='generator_detail'),
    # path('market/', include('market.urls')),
]
handler404 = 'pages.views.error_404_view'
