from django.contrib import admin
from .models import *


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_filter = ('ish_vaqti',)
    search_fields = ('ism',)


@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'kitob_soni', 'trik')
    list_editable = ('kitob_soni', 'trik')
    list_display_links = ('id', 'ism')
    search_fields = ('ism',)
    list_filter = ('trik',)

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'kitob_soni', 'kurs', 'bitruvchi')
    list_editable = ('kitob_soni', 'kurs', 'bitruvchi')
    list_display_links = ('ism',)
    list_filter = ('bitruvchi', 'kurs')
    list_per_page = 5
    search_fields = ('ism', 'id', 'kitob_soni')

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'sahifa', 'janr', 'muallif')
    list_editable = ('sahifa',)
    list_display_links = ('nom',)
    search_fields = ('id', 'nom')
    list_filter = ('janr',)
    autocomplete_fields = ('muallif',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    autocomplete_fields = ('talaba', 'kitob', 'admin')


