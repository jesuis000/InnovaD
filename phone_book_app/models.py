from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)

class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    number = models.CharField(max_length=200)
