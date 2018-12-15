from django.db import models

# Create your models here.


class MeasurementType(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    unit = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    measurement = models.ForeignKey(MeasurementType, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=6)
    timestamp = models.DateTimeField(auto_now_add=True)

