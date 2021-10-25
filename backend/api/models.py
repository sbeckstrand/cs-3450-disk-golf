from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_manager = models.BooleanField(default=False)
	is_drink_maister = models.BooleanField(default=False)
	is_sponsor = models.BooleanField(default=False)
	organization = models.CharField(max_length=120)
	
class Finance(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.PositiveIntegerField(default=0)
	contribution = models.PositiveIntegerField(default=0)
	
class Tournament(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	holes = models.PositiveIntegerField()
	participants = models.PositiveIntegerField()
	startDate = models.DateTimeField('Start Date')
	
	def __str__(self):
		return "{}".format(self.name)
	
class Score(models.Model):
	hole = models.PositiveIntegerField()
	value = models.IntegerField(default=0)
	player = models.ForeignKey(User, on_delete=models.CASCADE)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	
	def __str__(self):
		return "{}: Hole {}".format(self.tournament.name, self.hole)

class Drink(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	price = models.FloatField()
	type = models.CharField(max_length=30)
	
	def __str__(self):
		return "{}".format(self.name)

class DrinkOrder(models.Model):
	drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
	client = models.ForeignKey(User, on_delete=models.CASCADE)