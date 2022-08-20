from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(
        r'^details/(?P<vehicule_id>[0-9]+)/$',
        views.detail,
        name='details',
    ),
    url(
        r'^vehicule/$',
        views.vehicule,
        name='vehicule',
    ),
    url(
        r'^search/(?P<category_id>[0-9]+)/$',
        views.search,
        name='search',
    ),
    url(
        r'^order/$',
        views.order,
        name='order',
    ),
    url(
        r'^my_account/$',
        views.my_account,
        name='my_account',
    ),
]
