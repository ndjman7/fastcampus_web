from django.conf.urls import url

from . import views

app_name = 'movie'
urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^detail/$', views.detail, name='detail'),
]
