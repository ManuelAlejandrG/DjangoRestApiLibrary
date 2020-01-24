from django.db import models


class Editorial(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    

    class Meta:
        ordering = ('name',)


class Book(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    autor = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=100, blank=True, default='')
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)


