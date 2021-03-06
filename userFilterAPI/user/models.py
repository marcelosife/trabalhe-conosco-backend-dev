from django.db import models

class User(models.Model):
	id = models.CharField(max_length=50, primary_key=True);
	nome = models.CharField(max_length=50);
	username = models.CharField(max_length=50);
	relevancia = models.IntegerField( default = 0)
	
	def __str__(self):
		return self.nome
	
	def setRelevancia(self, relevancia):
		self.relevancia = relevancia;
		self.save()	
		