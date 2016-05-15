from django.db import models


class Localisation(models.Model):
    BOITE_DIAS = 'BD'
    NB_24_36 = 'NB2436'
    NB_6_6 = 'NB66'
    NB_GRANDS = 'NBG'
    CLASS_COUL = 'CC'

    TYPE_LOCALISATION = (
        (BOITE_DIAS, 'BOITE DIAS'),
        (NB_24_36, 'N&B 24.36'),
        (NB_6_6, 'N&B 6.6'),
        (NB_GRANDS, 'N&B Grands'),
        (CLASS_COUL, 'CLASS. COUL'),
    )

    numero = models.CharField(max_length=128)
    type = models.CharField(max_length=6, choices=TYPE_LOCALISATION)

    class Meta:
        unique_together = ("numero", "type")

    def __str__(self):
        return str(self.get_type_display() + ' n° ' + self.numero)


class MotCle(models.Model):
    mot = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.mot


class Diapo(models.Model):
    localisation = models.ForeignKey('Localisation')
    index = models.CharField(max_length=128, verbose_name='Emplacement')
    words = models.ManyToManyField('MotCle', blank=True)
    description = models.CharField(max_length=1000, blank=True)
    chemin = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        unique_together = ("localisation", "index")

    def __str__(self):
        return ("Localisation : %s -- Index %s : %s" % (self.localisation, self.index, self.description))


from photo.signals import *
