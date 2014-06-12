from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'smbp.views.home_page', name = 'home'),
)