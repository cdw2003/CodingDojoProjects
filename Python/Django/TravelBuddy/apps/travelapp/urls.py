from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^quotes$', views.index),
    url(r'^add$', views.quotes),
    url(r'^favorites/(?P<id>\d+)$', views.favorites),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^user/(?P<id>\d+)$', views.show_user)
]
