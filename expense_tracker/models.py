from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_credit = models.BooleanField(default=False)  # Credit or debit flag

    def __str__(self):
        return self.title

admin.site.register(Expense)