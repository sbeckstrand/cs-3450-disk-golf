from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrinkOrderViewSet, TournamentViewSet, ScoreViewSet, DrinkViewSet, create_auth, UserViewSet

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'drinks', DrinkViewSet)
router.register(r'orders', DrinkOrderViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
	path("", include(router.urls)),
	path("signup/", create_auth)
]