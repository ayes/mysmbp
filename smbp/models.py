from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User

class Kota(models.Model):
	kota = models.CharField('Nama Kota', max_length = 200)

	def __unicode__(self):
		return self.kota

	class Meta:
		db_table = 'tbkota'
		verbose_name_plural = '1. Kota'

class Kecamatan(models.Model):
	kota = models.ForeignKey(Kota, verbose_name='Nama Kota')
	kecamatan = models.CharField('Nama Kecamatan', max_length = 200)

	def __unicode__(self):
		return self.kecamatan

	class Meta:
		db_table = 'tbkecamatan'
		verbose_name_plural = '2. Kecamatan'

class Kelurahan(models.Model):
	kecamatan = models.ForeignKey(Kecamatan, verbose_name='Nama Kecamatan')
	kelurahan = models.CharField('Nama Kelurahan', max_length = 200)

	def __unicode__(self):
		return self.kelurahan

	class Meta:
		db_table = 'tbkelurahan'
		verbose_name_plural = '3. Kelurahan'

class Kriminalitas(models.Model):
	kriminalitas = models.CharField('Nama Kriminalitas', max_length = 200)

	def __unicode__(self):
		return self.kriminalitas

	class Meta:
		db_table = 'tbkriminalitas'
		verbose_name_plural = '4. Kriminalitas'

class KriminalitasDescription(models.Model):
	kota = models.ForeignKey(Kota)
	kecamatan = models.ForeignKey(Kecamatan)
	kelurahan = models.ForeignKey(Kelurahan)
	kriminalitas = models.ForeignKey(Kriminalitas)
	tanggal = models.DateTimeField('Tanggal dan Waktu')
	pelapor = models.ForeignKey(User)
	gambar = models.ImageField('Gambar', upload_to = 'smbp-description')
	isi = models.TextField('Keterangan', max_length=1024)

	def __unicode__(self):
		return self.kriminalitas.kriminalitas

	class Meta:
		db_table = 'tbkriminalitas_description'
		verbose_name_plural = '5. Input Data Kriminalitas'
