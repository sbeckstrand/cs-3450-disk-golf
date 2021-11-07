from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status, generics
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
	permission_classes = (permissions.IsAuthenticated,)
	
class ScoreViewSet(viewsets.ModelViewSet):
	serializer_class = ScoreSerializer
	queryset = Score.objects.all()
	permission_classes = (permissions.IsAuthenticated,)
	
class DrinkViewSet(viewsets.ModelViewSet):
	serializer_class = DrinkSerializer
	queryset = Drink.objects.all()
	permission_classes = (permissions.IsAuthenticated,)

class DrinkOrderViewSet(viewsets.ModelViewSet):
	serializer_class = DrinkOrderSerializer
	queryset = DrinkOrder.objects.all()
	permission_classes = (permissions.IsAuthenticated,)

# Currently returning all users, not sure how to limit the query to requested user
class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = (permissions.IsAuthenticated,)

class CurrentUserRetrieve(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_object(self):
		return self.request.user


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

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def createDrinkOrder(request):
	try:
		data = request.data
		drink = Drink.objects.get(id=data['drink_id'])
		user = User.objects.get(id=data['user_id'])
		order = DrinkOrder(client=user, drink=drink)
		order.save()

		return Response(status=status.HTTP_201_CREATED)
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)


	