from django.contrib import admin

from photo.models import Diapo, Boite, MotCle, Groupe


class BoiteAdmin(admin.ModelAdmin):
    list_display = ('repere',)

admin.site.register(Boite, BoiteAdmin)


class GroupeAdmin(admin.ModelAdmin):
    list_display = ('nom',)

admin.site.register(Groupe, GroupeAdmin)


class MotCleInline(admin.StackedInline):
    model = MotCle.groupe.through


class MotCleAdmin(admin.ModelAdmin):
    list_display = ('mot',)
    inlines = (MotCleInline,)

admin.site.register(MotCle, MotCleAdmin)


class DiapoInline(admin.StackedInline):
    model = Diapo.description.through


class DiapoAdmin(admin.ModelAdmin):
    list_display = ('boite', 'index',)
    inlines = (DiapoInline,)

admin.site.register(Diapo, DiapoAdmin)
