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
    )
]
