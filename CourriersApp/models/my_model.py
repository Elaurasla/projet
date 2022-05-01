from django.db import models

# Create your models here.

class Courrier(models.Model):
    num = models.PositiveIntegerField()
    date = models.DateField()
    date_emission = models.DateField()
    reference = models.TextField(blank = True)
    origine = models.CharField(max_length=100)
    objet = models.TextField(blank = True)
    bureau = models.CharField(max_length=100)

    def __str__(self):
        return self.reference