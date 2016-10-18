from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^add/$', views.add_bookmark, name='add_bookmark'),
    url(r'^bookmark_list/$', views.bookmark_list, name='bookmark_list')
]
