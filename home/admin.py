from django.contrib import admin
from .models import paket,musteri,sss
# Register your models here.
admin.site.register(paket)
admin.site.register(musteri)
admin.site.register(sss)
class paketAdmin(admin.ModelAdmin):
    list_display = ["paket_title","paket_ucrt",]
    search_fields = ["paket_title"]
    class Meta:
        model = paket