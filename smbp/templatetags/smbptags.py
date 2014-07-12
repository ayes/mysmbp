from django import template
from django.db.models import Sum
from smbp.models import *

register = template.Library()

@register.filter(name='wilayah')
def wilayah(kecamatan_id):
	kelurahan =  Kelurahan.objects.filter(kecamatan_id=kecamatan_id).order_by('kelurahan')
	return kelurahan

@register.filter(name='sumkriminalitas')
def sumkriminalitas(kriminalitas_id):
	total_kriminalitas =  KriminalitasDescription.objects.filter(kriminalitas_id=kriminalitas_id).count()
	return total_kriminalitas
	