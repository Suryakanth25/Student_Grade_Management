from django.db import models
from django.core.validators import MaxValueValidator, MaxLengthValidator

# Create your models here.
class Marks(models.Model):
    name = models.CharField(max_length=100)
    regno = models.IntegerField()
    sub1 = models.IntegerField(validators=[MaxValueValidator(100)])
    sub2 = models.IntegerField(validators=[MaxValueValidator(100)])
    sub3 = models.IntegerField(validators=[MaxValueValidator(100)])