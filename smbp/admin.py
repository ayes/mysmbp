from django.contrib import admin
from models import *

class KotaAdmin(admin.ModelAdmin):
	pass

class KecamatanAdmin(admin.ModelAdmin):
	pass

class KelurahanAdmin(admin.ModelAdmin):
	pass

class KriminalitasAdmin(admin.ModelAdmin):
	pass

class KriminalitasDescriptionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Kota, KotaAdmin)
admin.site.register(Kecamatan, KecamatanAdmin)
admin.site.register(Kelurahan, KelurahanAdmin)
admin.site.register(Kriminalitas, KriminalitasAdmin)
admin.site.register(KriminalitasDescription, KriminalitasDescriptionAdmin)
