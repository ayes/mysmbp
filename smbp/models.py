from django.db import models

class Kota(models.Model):
	nama_kota = models.CharField('Nama Kota', max_length = 200)

	def __unicode__(self):
		return self.nama_kota

	class meta:
		db_table = 'tbkota'

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
