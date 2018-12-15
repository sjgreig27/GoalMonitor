from django.db import models

# Create your models here.


class NicotineProduct(models.Model):

    class Meta:
        abstract = True

    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=280, blank=True, null=True)


class Cigarette(NicotineProduct):

    cost_in_pounds = models.DecimalField(max_digits=6, decimal_places=2, default=0.58)
    strength_in_mg = models.IntegerField(default=6)


class CigarettePacket(NicotineProduct):

    cost_in_pounds = models.DecimalField(max_digits=6, decimal_places=2, default=11.50)
    strength_in_mg = models.IntegerField(default=(6*20))


class Vapour(NicotineProduct):

    cost_in_pounds = models.DecimalField(max_digits=6, decimal_places=2, default=2.50)
    strength_in_mg_ml = models.IntegerField(default=3)
    volume = models.IntegerField(default=10)
