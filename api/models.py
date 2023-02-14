from django.db import models

##################################################################
# Model Persona, calculo de IMC. Class str devuele el nombre único 
##################################################################

class Persona(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    altura = models.FloatField()
    peso   = models.FloatField()


    def __str__(self):
        return self.nombre
