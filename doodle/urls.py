from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.new_meeting, name='new_meeting'), 
    url(r'^room/(?P<meeting_id>[0-9]+)/$', views.room, name='room'), 
    url(r'^(?P<meeting_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<meeting_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    url(r'^(?P<meeting_id>[0-9]+)/vote/$', views.vote, name='vote'),
]