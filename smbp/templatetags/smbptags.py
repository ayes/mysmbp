from django import template
from smbp.models import *

register = template.Library()

@register.filter(name='wilayah')
def wilayah(kecamatan_id):
	kelurahan =  Kelurahan.objects.filter(kecamatan_id=kecamatan_id).order_by('kelurahan')
	return kelurahan