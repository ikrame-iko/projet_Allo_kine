from django.db import models

# Create your models here.
class Client(models.Model):
    nom_cl = models.CharField(max_length=30)
    prenom_cl = models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    telephone = models.IntegerField()
    adresse=models.CharField(max_length=30)