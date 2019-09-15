"""wua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, market_list, analytics_graph, analytics_map, market_create, gen_detail, about, analytics_other

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', post_list, name='HOME | WUA'),
    path('market/create/', market_create, name='market_create'),
    path('market/list/', market_list, name='market_list'),
    path('market/details/<int:pk>/', gen_detail, name='generator_detail'),
    path('analytics/graph/', analytics_graph, name='analytics_graph'),
    path('analytics/map/', analytics_map, name='analytics_map'),
    path('about/', about, name='about_us'),
    path('analytics/other/', analytics_other, name='analytics_other'),

    # path('market/', include('market.urls')),
]
handler404 = 'pages.views.error_404_view'
