from django.db import models

# Create your models here.

class Equation(models.Model):
    value_a = models.IntegerField('A', max_length=3)
    value_b = models.IntegerField('B', max_length=3)
    value_c = models.IntegerField('C', max_length=3)

    def __str__(self):
        return f"A: {self.value_a}, B: {self.value_b}, C: {self.value_c} "

