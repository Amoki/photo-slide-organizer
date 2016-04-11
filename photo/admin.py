from django.contrib import admin

from photo.models import Diapo, Boite, MotCle


class BoiteAdmin(admin.ModelAdmin):
    list_display = ('repere',)

admin.site.register(Boite, BoiteAdmin)


class MotCleAdmin(admin.ModelAdmin):
    list_display = ('mot',)

admin.site.register(MotCle, MotCleAdmin)


class DiapoAdmin(admin.ModelAdmin):
    list_display = ('boite', 'index', 'description')

admin.site.register(Diapo, DiapoAdmin)
