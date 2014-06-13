from django.contrib import admin
from models import Kota, Kecamatan, Kelurahan

class KotaAdmin(admin.ModelAdmin):
	pass

class KecamatanAdmin(admin.ModelAdmin):
	pass

class KelurahanAdmin(admin.ModelAdmin):
	pass

admin.site.register(Kota, KotaAdmin)
admin.site.register(Kecamatan, KecamatanAdmin)
admin.site.register(Kelurahan, KelurahanAdmin)
