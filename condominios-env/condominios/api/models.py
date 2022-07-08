from django.db import models

# Create your models here.

class Condominium(models.Model):
    id_condominium = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

class House(models.Model):
    id_house = models.AutoField(primary_key=True)
    headline = models.IntegerField()
    fk_condominium = models.ForeignKey(Condominium, on_delete=models.CASCADE)

class Resident(models.Model):
    id_resident = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    date_birth = models.DateTimeField()
    mail = models.EmailField()

class Residence(models.Model):
    id_residence = models.AutoField(primary_key=True)
    date_init = models.DateTimeField()
    date_end = models.DateTimeField()
    fk_resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    fk_house = models.ForeignKey(House, on_delete=models.CASCADE)