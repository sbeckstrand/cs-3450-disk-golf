from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from api.models import Tournament, Score, Drink, Finance, DrinkOrder, SponsorLogo, Sponsorship


class FinanceInline(admin.StackedInline):
	model = Finance
	can_delete = False
	verbose_name_plural = 'finance'
	
class UserAdmin(BaseUserAdmin):
	inlines = [FinanceInline]
	
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tournament)
admin.site.register(Score)
admin.site.register(Drink)
admin.site.register(DrinkOrder)
admin.site.register(SponsorLogo)
admin.site.register(Sponsorship)
