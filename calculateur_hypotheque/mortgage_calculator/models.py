from django.db import models

# Create your models here.
class CityTaxes(models.Model):
    city_name = models.TextField()
    city_taxe = models.DecimalField(max_digits=6, decimal_places=5)
    city_school_taxe = models.DecimalField(max_digits=6, decimal_places=5)
    # city_water_taxe = models.DecimalField(max_digits=5, decimal_places=2)