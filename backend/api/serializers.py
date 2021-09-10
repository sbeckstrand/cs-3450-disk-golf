from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tournament, Score, Drink

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