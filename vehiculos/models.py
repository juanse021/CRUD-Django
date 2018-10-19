from django.db import models

class Carro(models.Model):
	image = models.ImageField(upload_to='img/', max_length=100)
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=30)
	precio = models.FloatField()


	def __str__(self):
		return self.marca + " " + self.modelo