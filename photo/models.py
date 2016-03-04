from django.db import models


class Boite(models.Model):
    repere = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.repere)


class Groupe(models.Model):
    nom = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.nom


class MotCle(models.Model):
    mot = models.CharField(max_length=128, unique=True)
    groupe = models.ManyToManyField('Groupe', blank=True)

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
        motCles = self.description.all()
        return ("Repère %s Index %s : %s" % (self.boite, self.index, ', '.join(str(m) for m in motCles)))
