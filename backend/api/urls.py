from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TournamentViewSet, ScoreViewSet, DrinkViewSet

router = DefaultRouter()
router.register(r'Tournament', TournamentViewSet)
router.register(r'Score', ScoreViewSet)
router.register(r'Drink', DrinkViewSet)

urlpatterns = [
	path("", include(router.urls))
]