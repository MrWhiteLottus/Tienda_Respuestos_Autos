from django.db import models

# Create your models here.


class Auto(models.Model):
    marca = models.CharField(primary_key=True, max_length=20)
    modelo = models.CharField(max_length=20)
    anno = models.PositiveIntegerField()
    id_auto = models.ForeignKey('Auto',on_delete=models.CASCADE, db_column='idAuto')
    num_puertas = models.PositiveIntegerField()
    motor = models.BooleanField(True)
    activo = models.IntegerField()
    
    def __str__(self):
     return str(self.marca)+" "+str(self.modelo)