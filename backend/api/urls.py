from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrinkOrderViewSet, TournamentViewSet, ScoreViewSet, DrinkViewSet

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'drinks', DrinkViewSet)
router.register(r'orders', DrinkOrderViewSet)

urlpatterns = [
	path("", include(router.urls))
]