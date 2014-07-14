from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from smbp.models import *
from smbp.forms import *

def home_page(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard');
	else:
		return render_to_response('login-page.html',{}, RequestContext(request))

@login_required()
def get_profile(request):
	try:
		profile = Profile.objects.get(user=request.user)
	except:
		profile = {}

	return profile


@login_required()
def dashboard(request):
	return render_to_response('dashboard-main.html', {'profile':get_profile(request)}, RequestContext(request))

@login_required()
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

@login_required()
def potensi(request):
	if request.method == 'POST': 
		form = PotensiForm(request.POST)
		judul = request.POST.get('judul', '')
		tanggal = request.POST.get('tanggal', '')
		waktu = request.POST.get('waktu', '')
		potensi = request.POST.get('potensi', '')
		if form.is_valid():
			tglwkt = tanggal + ' ' + waktu
			potensi = Potensi(judul=judul, pelapor=request.user, tanggal=tglwkt, potensi=potensi)
			potensi.save()
			return HttpResponseRedirect('/dashboard/potensi/')
	else:
		form = PotensiForm()
	return render_to_response('dashboard-potensi.html', {'form': form,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def kejadian(request):
	if request.method == 'POST': 
		#form = KejadianForm(request.POST)
		form = KejadianForm(request.POST, request.FILES)
		kecamatan = request.POST.get('kecamatan', '')
		kelurahan = request.POST.get('kelurahan', '')
		kriminalitas = request.POST.get('kriminalitas', '')
		tanggal = request.POST.get('tanggal', '')
		waktu =request.POST.get('waktu', '')
		#gambar = request.POST, request.FILES
		isi = request.POST.get('isi', '')
		if form.is_valid():
			kec = Kecamatan.objects.get(pk=kecamatan)
			kel = Kelurahan.objects.get(pk=kelurahan)
			krim = Kriminalitas.objects.get(pk=kriminalitas)
			tglwkt = tanggal + ' ' + waktu
			kejadian = KriminalitasDescription(kecamatan=kec, kelurahan=kel, kriminalitas=krim, tanggal=tglwkt, pelapor=request.user, gambar=request.FILES['gambar'], isi=isi)
			kejadian.save()
			return HttpResponseRedirect('/dashboard/kejadian/')
	else:
		try:
			kecamatan = Kecamatan.objects.all()
		except:
			kecamatan = {}
		try:
			kelurahan = Kelurahan.objects.all()
		except:
			kelurahan = {}
		try:
			kriminalitas = Kriminalitas.objects.all()
		except:
			kriminalitas = {}
		form = KejadianForm()
	return render_to_response('dashboard-kejadian.html', 
		{'form': form, 'kecamatan': kecamatan, 'kelurahan': kelurahan, 'kriminalitas': kriminalitas,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def live_potensi(request):
	try:
		live_potensi = Potensi.objects.all().order_by('-id')[:20]
	except:
		live_potensi = {}
	return render_to_response('dashboard-live-potensi.html', {'live_potensi':live_potensi,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def live_kejadian(request):
	try:
		live_kejadian = KriminalitasDescription.objects.select_related().order_by('-id')[:20]
	except:
		live_kejadian = {}
	return render_to_response('dashboard-live-kejadian.html', {'live_kejadian':live_kejadian,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def wilayah(request):
	try:
		kecamatan = Kecamatan.objects.all().order_by('kecamatan')
	except:
		kecamatan = {}
	return render_to_response('dashboard-wilayah.html', {'kecamatan':kecamatan,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def show_wilayah_kelurahan(request, kelurahan_id = None):
	try:
		show_wilayah_kelurahan = KriminalitasDescription.objects.select_related().filter(kelurahan_id=kelurahan_id)
	except:
		show_wilayah_kelurahan = {}
	return render_to_response('dashboard-wilayah-kelurahan.html', {'show_wilayah_kelurahan':show_wilayah_kelurahan,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def data_kriminalitas(request):
	try:
		data_kriminalitas = KriminalitasDescription.objects.select_related()
	except:
		data_kriminalitas = {}

	return render_to_response('dashboard-data-kriminalitas.html', {'data_kriminalitas':data_kriminalitas,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def rekapitulasi_kriminalitas(request):
	try:
		kriminalitas = Kriminalitas.objects.all().order_by('id')
	except:
		kriminalitas = {}

	#try:
		rekapitulasi_kriminalitas = KriminalitasDescription.objects.select_related().filter(kriminalitas_id=kriminalitas_id).aggregate(Sum('field_name'))
	#except:
	#	rekapitulasi_kriminalitas = {}

	return render_to_response('dashboard-rekapitulasi-kriminalitas.html', {'kriminalitas':kriminalitas,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def profile(request):
	if request.method == 'POST': 
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				profile = Profile.objects.get(user=request.user)
				profile.gambar= request.FILES['gambar']
				profile.save()
				return HttpResponseRedirect('/dashboard/profile/')
			except:
				profile = Profile(user=request.user, gambar=request.FILES['gambar'])
				profile.save()
	else:
		form = ProfileForm()
	return render_to_response('dashboard-profile.html', 
		{'form': form,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def print_data_kriminalitas(request):
	try:
		data_kriminalitas = KriminalitasDescription.objects.select_related()
	except:
		data_kriminalitas = {}

	return render_to_response('dashboard-print-data-kriminalitas.html', {'data_kriminalitas':data_kriminalitas,'profile':get_profile(request)}, RequestContext(request))

@login_required()
def print_rekapitulasi_kriminalitas(request):
	try:
		kriminalitas = Kriminalitas.objects.all().order_by('id')
	except:
		kriminalitas = {}

	#try:
		rekapitulasi_kriminalitas = KriminalitasDescription.objects.select_related().filter(kriminalitas_id=kriminalitas_id).aggregate(Sum('field_name'))
	#except:
	#	rekapitulasi_kriminalitas = {}

	return render_to_response('dashboard-print-rekapitulasi-kriminalitas.html', {'kriminalitas':kriminalitas,'profile':get_profile(request)}, RequestContext(request))