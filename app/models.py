from django.db import models

# Create your models here.

class Committee(models.Model):
    name = models.CharField(max_length=50)
    chair = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Document(models.Model):
    lims_number = models.CharField(max_length=30)
    actions_date = models.DateField(blank=True, null=True)
    referral = models.ManyToManyField(Committee, verbose_name="Committee Referral", null=True, blank=True)
    description = models.TextField(blank=True, null=True, default="")
    issues = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return self.lims_number

# #     
# #* LIMS number
# * Deemed Approved/Action Date
# * Referral
# * Descriptive Column
# * Issues Column
# * Type (Contract/Reprogramming)
    