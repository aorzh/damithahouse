from django.conf.urls import patterns, url
from room import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^item/(?P<item_id>\d+)/$', views.single_room, name='single_room'),
                       )
