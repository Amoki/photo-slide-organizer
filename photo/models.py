from django.db import models


class Boite(models.Model):
    numero = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.numero)


class MotCle(models.Model):
    mot = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.mot


class Diapo(models.Model):
    boite = models.ForeignKey('Boite')
    index = models.PositiveIntegerField()
    description = models.ManyToManyField('MotCle', blank=True)
    chemin = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        unique_together = ("boite", "index")

    def __str__(self):
        return ("%s/%s" % (self.boite, self.index))
