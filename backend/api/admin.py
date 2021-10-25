from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from api.models import Tournament, Score, Drink, Role, Finance
from backend.api.models import DrinkOrder


class RoleInline(admin.StackedInline):
	model = Role
	can_delete = False
	verbose_name_plural = 'role'

class FinanceInline(admin.StackedInline):
	model = Finance
	can_delete = False
	verbose_name_plural = 'finance'
	
class UserAdmin(BaseUserAdmin):
	inlines = (RoleInline, FinanceInline)
	
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tournament)
admin.site.register(Score)
admin.site.register(Drink)
admin.site.register(DrinkOrder)
