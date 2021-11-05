from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DrinkOrder, Tournament, Score, Drink

class TournamentSerializer(serializers.ModelSerializer):
	
	class Meta: 
		model = Tournament
		fields = ("id", "name", "description", "holes", "participants", "startDate")
		
class ScoreSerializer(serializers.ModelSerializer):
	
	class Meta: 
		model = Score
		fields = ("id", "hole", "value", "player", "tournament")
		
class DrinkSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Drink
		fields = ("id", "name", "type", "description", "price")

class DrinkOrderSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = DrinkOrder
		fields = ("id", "drink", "client")

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	def create(self, data):
		user = User.objects.create_user(
			username=data['username'],
			email=data['email'],
			password=data['password']
		)

		return user
	
	class Meta:
		model = User
		fields = ("id", "username", "email", "password" )