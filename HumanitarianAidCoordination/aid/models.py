from django.db import models

# Create your models here.
from django.db import models

class Beneficiary(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AidItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity_available = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Distribution(models.Model):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    item = models.ForeignKey(AidItem, on_delete=models.CASCADE)
    quantity_distributed = models.PositiveIntegerField()
    distribution_date = models.DateField()

    def __str__(self):
        return f"{self.item.name} to {self.beneficiary.name}"
