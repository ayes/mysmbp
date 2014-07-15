from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'smbp.views.home_page', name = 'home'),
	url(r'^accounts/login$', 'django.contrib.auth.views.login', {'template_name': 'login-page.html'}),
	
	url(r'^dashboard/?$', 'smbp.views.dashboard'),
	url(r'^dashboard/logout/?$','smbp.views.logout'),

	url(r'^dashboard/profile/?','smbp.views.profile'),
	url(r'^dashboard/potensi/?$','smbp.views.potensi'),
	url(r'^dashboard/kejadian/?','smbp.views.kejadian'),
	url(r'^dashboard/live-potensi/?','smbp.views.live_potensi'),
	url(r'^dashboard/live-kejadian/?','smbp.views.live_kejadian'),
	url(r'^dashboard/wilayah/?$','smbp.views.wilayah'),
	url(r'^dashboard/wilayah/kelurahan/(?P<kelurahan_id>[\d]+)$', 'smbp.views.show_wilayah_kelurahan'),
	url(r'^dashboard/data-kriminalitas/?$','smbp.views.data_kriminalitas'),
	url(r'^dashboard/data-kriminalitas/print/?','smbp.views.print_data_kriminalitas'),
	url(r'^dashboard/rekapitulasi-kriminalitas/?$','smbp.views.rekapitulasi_kriminalitas'),
	url(r'^dashboard/rekapitulasi-kriminalitas/print/?','smbp.views.print_rekapitulasi_kriminalitas'),

	url(r'^dashboard/potensi-konflik/detail/(?P<pk_id>[\d]+)$','smbp.views.potensi_konflik_detail'),

)