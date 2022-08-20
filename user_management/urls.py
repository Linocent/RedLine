from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'log_in/$', views.log_in, name='log_in'),
    url(r'log_out/$', views.log_out, name='log_out'),
]
