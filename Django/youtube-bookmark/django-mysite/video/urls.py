from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.category_video_list, name='category_video_list'),
    url(r'^edit/$', views.category_edit, name='category_edit'),
    url(r'^(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', views.video_list, name='video_list'),
]
