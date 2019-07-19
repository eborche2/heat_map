from django.db import models


class IpvFour(models.Model):
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)


class IpvSix(models.Model):
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)