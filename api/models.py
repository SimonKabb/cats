from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    birth_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name