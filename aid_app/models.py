# models.py

from django.db import models

class Beneficiary(models.Model):
    # Define the fields for the Beneficiary model
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add other fields...

    def __str__(self):
        return self.name

class AidItem(models.Model):
    # Define the fields for the AidItem model
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    # Add other fields...

    def __str__(self):
        return self.name

class Distribution(models.Model):
    # Define the fields for the Distribution model
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    aid_item = models.ForeignKey(AidItem, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other fields...

    def __str__(self):
        return f"{self.beneficiary.name} - {self.aid_item.name}"

