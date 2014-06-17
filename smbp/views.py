from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth

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
	return render_to_response('dashboard-wilayah.html', {}, RequestContext(request))
