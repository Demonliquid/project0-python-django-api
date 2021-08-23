from django.db import models

class Cryptocurrency(models.Model):
    cryptocurrency_name = models.CharField(max_length=100)
    cryptocurrency_subtitle = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    market_number = models.CharField(max_length=100)
    market_unit = models.CharField(max_length=100)
    change = models.CharField(max_length=100)

    def __str__(self):
        return self.cryptocurrency_name