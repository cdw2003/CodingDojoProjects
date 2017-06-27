from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.index, name = "books"),
    url(r'^add_book$', views.new_book),
    url(r'^process$', views.add_book),
    url(r'^books/(?P<id>\d+)$', views.show_books),
    url(r'^reviews/(?P<id>\d+)$', views.reviews),
    url(r'^remove/(?P<id>\d+)$', views.remove_review),
    url(r'^user/(?P<id>\d+)$', views.show_user)
]
