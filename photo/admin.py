from django.contrib import admin

from photo.models import Diapo, Localisation, MotCle


class LocalisationAdmin(admin.ModelAdmin):
    list_display = ('type', 'numero')

admin.site.register(Localisation, LocalisationAdmin)


class MotCleAdmin(admin.ModelAdmin):
    list_display = ('mot',)

admin.site.register(MotCle, MotCleAdmin)


class DiapoAdmin(admin.ModelAdmin):
    list_display = ('localisation', 'index', 'description')

admin.site.register(Diapo, DiapoAdmin)
