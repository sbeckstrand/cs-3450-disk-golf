from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import DrinkOrderSerializer, TournamentSerializer, ScoreSerializer, DrinkSerializer, UserSerializer
from .models import DrinkOrder, Tournament, Score, Drink, Role
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core import serializers

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

class DrinkOrderViewSet(viewsets.ModelViewSet):
	serializer_class = DrinkOrderSerializer
	queryset = DrinkOrder.objects.all()

# Currently returning all users, not sure how to limit the query to requested user
class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def create_auth(request):
	serialized = UserSerializer(data=request.data)
	
	if serialized.is_valid():
		serialized.create(request.data)
		return Response(serialized.data, status=status.HTTP_201_CREATED)
	else:
		print(serialized._errors)
		return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
		
# TODO FIX THIS SHIT
@csrf_exempt
def createDrinkOrder(request):
	user = request.user
	print(request.POST.get("name"))
	id = request.POST.get("id")
	drink = Drink.objects.get(pk = id )
	order = DrinkOrder(client=user,drink=drink)
	order.save()


	