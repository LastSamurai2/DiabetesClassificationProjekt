from django.db import models

# Create your models here.
class DiabetesData(models.Model):
    pregnancies = models.IntegerField(null=False, blank=False)
    glucose = models.IntegerField(null=False, blank=False)
    blood_preasure = models.IntegerField(null=False, blank=False)
    skin_thickness = models.IntegerField(null=False, blank=False)
    insulin = models.IntegerField(null=False, blank=False)
    bmi = models.FloatField(null=False, blank=False)
    diabetes_pedigree_function = models.FloatField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    outcome = models.IntegerField(null=False, blank=False)