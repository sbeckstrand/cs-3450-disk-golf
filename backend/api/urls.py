from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParticipantViewSet, toggleTournamentActive, DrinkOrderViewSet, SponsorLogoViewSet, SponsorshipViewSet, TournamentViewSet, ScoreViewSet, DrinkViewSet, create_auth, UserViewSet, createDrinkOrder, CurrentUserRetrieve, toggleTournamentActive, updateBalance, updateRole, SponsorLogoView

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'drinks', DrinkViewSet)
router.register(r'orders', DrinkOrderViewSet)
router.register(r'users', UserViewSet)
router.register(r'sponsorships', SponsorshipViewSet)
router.register(r'participants', ParticipantViewSet)



urlpatterns = [
	path("", include(router.urls)),
	path("signup/", create_auth),
	path('current_user/', CurrentUserRetrieve.as_view(), name='user-data'),
	path('current_user/<int:id>', CurrentUserRetrieve.as_view(), name='user-data'),
	path("orderDrink/", createDrinkOrder),
	path("updateRole/", updateRole),
	path("updateBalance/", updateBalance),
	path('logo/', SponsorLogoView.as_view(), name='logo-upload'),
	path('toggleTournament/', toggleTournamentActive)
]