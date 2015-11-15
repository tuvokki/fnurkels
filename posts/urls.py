from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /posts/5/
    url(r'^full/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^comment/(?P<article_id>[0-9]+)/$', views.comment, name='comment'),
]
