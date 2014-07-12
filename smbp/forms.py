from django import forms
from django.forms import ModelForm
from smbp.models import *

class PotensiForm(ModelForm):
	class Meta:
		model = Potensi
		fields = ['judul', 'tanggal', 'potensi']

class KejadianForm(ModelForm):
	class Meta:
		model = KriminalitasDescription
		fields = ['kecamatan', 'kelurahan', 'kriminalitas', 'tanggal', 'gambar', 'isi']

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['gambar',]