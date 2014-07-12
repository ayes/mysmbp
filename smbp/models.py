from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User

class Kecamatan(models.Model):
	kecamatan = models.CharField('Nama Kecamatan', max_length = 200)

	def __unicode__(self):
		return self.kecamatan

	class Meta:
		db_table = 'tbkecamatan'
		verbose_name_plural = '1. Kecamatan'

class Kelurahan(models.Model):
	kecamatan = models.ForeignKey(Kecamatan)
	kelurahan = models.CharField('Nama Kelurahan', max_length = 200)

	def __unicode__(self):
		return self.kelurahan

	class Meta:
		db_table = 'tbkelurahan'
		verbose_name_plural = '2. Kelurahan'

class Potensi(models.Model):
	judul = models.CharField('Judul', max_length = 200)
	pelapor = models.ForeignKey(User)
	tanggal = models.DateTimeField('Tanggal dan Waktu')
	potensi = models.TextField('Keterangan Potensi', max_length=1024)

	def __unicode__(self):
		return self.judul

	class Meta:
		db_table = 'tbpotensi'
		verbose_name_plural = '3. Potensi'


class Kriminalitas(models.Model):
	kriminalitas = models.CharField('Nama Kriminalitas', max_length = 200)

	def __unicode__(self):
		return self.kriminalitas

	class Meta:
		db_table = 'tbkriminalitas'
		verbose_name_plural = '4. Kriminalitas'

class KriminalitasDescription(models.Model):
	kecamatan = models.ForeignKey(Kecamatan)
	kelurahan = models.ForeignKey(Kelurahan)
	kriminalitas = models.ForeignKey(Kriminalitas)
	tanggal = models.DateTimeField('Tanggal dan Waktu')
	pelapor = models.ForeignKey(User)
	gambar = models.ImageField('Gambar', upload_to = 'smbp-description')
	isi = models.TextField('Keterangan', max_length=1024)

	def __unicode__(self):
		return self.kriminalitas.kriminalitas

	def gambar_(self):
		return '<img src="/media/%s"/ width="100px">' % self.gambar
	gambar_.allow_tags = True

	class Meta:
		db_table = 'tbkriminalitas_description'
		verbose_name_plural = '5. Input Data Kriminalitas'

class Profile(models.Model):
	user = models.ForeignKey(User)
	gambar = models.ImageField('Gambar', upload_to = 'smbp-profile')

	def __unicode__(self):
		return self.user.user

	def gambar_(self):
		return '<img src="/media/%s"/ width="100px">' % self.gambar
	gambar_.allow_tags = True

	class Meta:
		db_table = 'tbprofile'
		verbose_name_plural = '6. Profile'