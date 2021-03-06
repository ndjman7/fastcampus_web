from django.conf.urls import url

from . import views

app_name = 'poll'
urlpatterns = [
        # ex: /polls/
        url(r'^$', views.index, name='index'),
        # ex: /polls/5/
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        url(r'^(?P<question_id>[0-9]+)/add_choice/$', views.add_choice, name='add_choice'),

]
