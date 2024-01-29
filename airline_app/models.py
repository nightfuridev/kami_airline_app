from django.db import models
from math import log10

class Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    passengers = models.IntegerField(default=0)

    @property
    def fuel_tank_capacity(self):
        return self.id * 200

    @property
    def fuel_consumption_per_minute(self):
        return log10(self.id) * 0.80 + self.passengers * 0.002

    @property
    def max_minutes_to_fly(self):
        return self.fuel_tank_capacity / self.fuel_consumption_per_minute