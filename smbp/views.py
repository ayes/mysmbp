from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from smbp.models import *

def home_page(request):
	return render_to_response('login-page.html',{}, RequestContext(request))

@login_required()
def dashboard(request):
	return render_to_response('dashboard-main.html', {}, RequestContext(request))

@login_required()
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

@login_required()
def wilayah(request):
	try:
		wilayah = Kelurahan.objects.select_related()
	except:
		wilayah = {}

	return render_to_response('dashboard-wilayah.html', {'wilayah':wilayah}, RequestContext(request))

@login_required()
def data_kriminalitas(request):
	try:
		data_kriminalitas = KriminalitasDescription.objects.select_related()
	except:
		data_kriminalitas = {}

	return render_to_response('dashboard-data-kriminalitas.html', {'data_kriminalitas':data_kriminalitas}, RequestContext(request))

@login_required()
def rekapitulasi_kriminalitas(request):
	try:
		kriminalitas = Kriminalitas.objects.all()
	except:
		kriminalitas = {}

	try:
		rekapitulasi_kriminalitas = KriminalitasDescription.objects.select_related()
	except:
		rekapitulasi_kriminalitas = {}

	return render_to_response('dashboard-rekapitulasi-kriminalitas.html', {'kriminalitas':kriminalitas,'rekapitulasi_kriminalitas':rekapitulasi_kriminalitas}, RequestContext(request))
