from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.noNinjas),
    url(r'^ninjas$', views.helloNinjas),
    url(r'^ninjas/(?P<color>\w+)$', views.colorNinjas)
]
