from django.db import models
from django.contrib.auth.models import User

class Kota(models.Model):
	nama_kota = models.CharField('Nama Kota', max_length = 200)

	def __unicode__(self):
		return self.nama_kota

	class meta:
		db_table = 'tbkota'
		verbose_name_plural = 'Kota'

class Kecamatan(models.Model):
	nama_kecamatan = models.CharField('Nama Kecamatan', max_length = 200)

	def __unicode__(self):
		return self.nama_kecamatan

	class meta:
		db_table = 'tbkecamatan'

class Kelurahan(models.Model):
	nama_kelurahan = models.CharField('Nama Kelurahan', max_length = 200)

	def __unicode__(self):
		return self.nama_kelurahan

	class meta:
		db_table = 'tbkelurahan'

class Kriminalitas(models.Model):
	nama_kriminalitas = models.CharField('Nama Kriminalitas', max_length = 200)

	def __unicode__(self):
		return self.nama_kriminalitas

	class meta:
		db_table = 'tbkriminalitas'

class KriminalitasDescription(models.Model):
	nama_kota = models.ForeignKey(Kota)
	nama_kecamatan = models.ForeignKey(Kecamatan)
	nama_kelurahan = models.ForeignKey(Kelurahan)
	nama_kriminalitas = models.ForeignKey(Kriminalitas)
	tanggal = models.DateTimeField('Tanggal dan Waktu')
	pelapor = models.ForeignKey(User)
	gambar = models.ImageField(u'Gambar', upload_to = 'smbp-description')
	isi = models.TextField('Keterangan', max_length=1024)

	def __unicode__(self):
		return self.nama_kriminalitas.nama_kriminalitas

	class meta:
		db_table = 'tbkriminalitas_description'
