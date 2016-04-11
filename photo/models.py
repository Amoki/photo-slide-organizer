from django.db import models


class Boite(models.Model):
    repere = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.repere)


class MotCle(models.Model):
    mot = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.mot


class Diapo(models.Model):
    boite = models.ForeignKey('Boite')
    index = models.PositiveIntegerField()
    words = models.ManyToManyField('MotCle', blank=True)
    description = models.CharField(max_length=1000, blank=True)
    chemin = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        unique_together = ("boite", "index")

    def __str__(self):
        return ("Repère %s Index %s : %s" % (self.boite, self.index, self.description))


from photo.signals import *
