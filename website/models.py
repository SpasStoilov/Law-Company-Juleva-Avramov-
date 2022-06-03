# https://docs.djangoproject.com/en/4.0/ref/models/fields/   джанго документация
from django.db import models


class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    information = models.TextField(max_length=600)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LegalServices(models.Model):
    service = models.CharField(max_length=100)
    information = models.TextField(max_length=None, null=True, blank=True)

    def __str__(self):
        return f"{self.service}"


class Clients(models.Model):
    client_first_name = models.CharField(max_length=30)
    client_last_name = models.CharField(max_length=30)
    text = models.TextField(max_length=600)
    number = models.IntegerField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    lawyer_name = models.ForeignKey(
        Employees, on_delete=models.CASCADE
    )
    email_client = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'{self.client_first_name} {self.client_last_name}'





