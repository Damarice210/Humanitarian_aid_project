# from django.db import models

# class AidItem(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     quantity_available = models.IntegerField()

#     def __str__(self):
#         return self.name


# class DistributionCenter(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     contact_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.name


# class AidDistribution(models.Model):
#     aid_item = models.ForeignKey(AidItem, on_delete=models.CASCADE)
#     distribution_center = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)
#     quantity_distributed = models.IntegerField()
#     date_of_distribution = models.DateField()

#     def __str__(self):
#         return f"{self.aid_item.name} distributed to {self.distribution_center.name} on {self.date_of_distribution}"

#     class Meta:
#         unique_together = ('aid_item', 'distribution_center', 'date_of_distribution')

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
