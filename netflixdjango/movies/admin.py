from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display=["id","filmismi","Kategori"]
    list_display_links=["id"]
    list_filter=["Kategori"]
    search_fields=["filmismi","Kategori_name"]
    list_per_page=2
    list_editable=["filmismi"]
# istersek yanlarına virgül atabiliriz.
# Register your models here.
admin.site.register(Movies, MovieAdmin)
admin.site.register(Kategori)
admin.site.register(Tur)
admin.site.register(Izlenenler)
