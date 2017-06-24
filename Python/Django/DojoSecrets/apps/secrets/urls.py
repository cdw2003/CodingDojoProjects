from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^secrets$', views.index, name = "secrets"),
    url(r'^view$', views.secrets),
    url(r'^like/(?P<id>\d+)$', views.like),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^popular$', views.popular),
]
