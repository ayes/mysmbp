from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'smbp.views.home_page', name = 'home'),
	url(r'^accounts/login$', 'django.contrib.auth.views.login', {'template_name': 'login-page.html'}),
	
	url(r'^dashboard/?$', 'smbp.views.dashboard'),
	url(r'^dashboard/logout/?$','smbp.views.logout'),

	url(r'^dashboard/wilayah/?','smbp.views.wilayah'),
	url(r'^dashboard/data-kriminalitas/?','smbp.views.data_kriminalitas'),
	url(r'^dashboard/rekapitulasi-kriminalitas/?','smbp.views.rekapitulasi_kriminalitas'),

)