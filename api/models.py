from django.db import models

class Items(models.Model):
    name=models.CharField(max_length=205)
    category=models.CharField(max_length=205)
    isCredit = models.BooleanField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name
# Create your models here.
