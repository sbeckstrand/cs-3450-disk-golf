from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DrinkOrderSerializer, TournamentSerializer, ScoreSerializer, DrinkSerializer
from .models import DrinkOrder, Tournament, Score, Drink

# Create your views here.
class TournamentViewSet(viewsets.ModelViewSet):
	serializer_class = TournamentSerializer
	queryset = Tournament.objects.all()
	
class ScoreViewSet(viewsets.ModelViewSet):
	serializer_class = ScoreSerializer
	queryset = Score.objects.all()
	
class DrinkViewSet(viewsets.ModelViewSet):
	serializer_class = DrinkSerializer
	queryset = Drink.objects.all()

class DrinkOrderViewSet(viewsets):
	serializer_class = DrinkOrderSerializer
	queryset = DrinkOrder.objects.all()