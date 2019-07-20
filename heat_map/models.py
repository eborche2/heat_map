from django.db import models


class Ipv(models.Model):
    latitude = models.DecimalField(db_index=True, max_digits=12, decimal_places=6)
    longitude = models.DecimalField(db_index=True, max_digits=12, decimal_places=6)
    ipv4 = models.IntegerField(blank=True, null=True, default=0)
    ipv6 = models.IntegerField(blank=True, null=True, default=0)
    level = models.IntegerField(blank=True, null=True, default=1)


