from django.conf.urls import patterns, url
from bunker import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'^users/(?P<user_id>\d+)/$', views.personal, name="personal"),
	url(r'^new$', views.bunkform, name="bunkform"),
)
