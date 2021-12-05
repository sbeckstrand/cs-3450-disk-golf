# Generated by Django 3.1.2 on 2020-10-16 22:46

from django.db import migrations, models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.hashers import make_password



def populate_db(apps, schema_editor):

	Group = apps.get_model('auth', 'Group')
	SponsorLogo = apps.get_model('api', 'SponsorLogo')
	Finance = apps.get_model('api', 'Finance')

	User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
	

	manager = User(username="manager",email="manager@diskgolfapp.com",password=make_password('manager'))
	manager.save()

	mFinance = Finance(user=manager)
	mFinance.save()

	User.objects.create(
		username="drinkster",
		email="drinkster@diskgolfapp.com",
		password=make_password('drinkster'),
	)

	drinkster = User.objects.get(username="drinkster")
	drinkster.save()

	dFinance = Finance(user=drinkster)
	dFinance.save()

	User.objects.create(
		username="sponsor",
		email="sponsor@diskgolfapp.com",
		password=make_password('sponsor'),
	)

	sponsor = User.objects.get(username="sponsor")
	sponsor.save()

	sFinance = Finance(user=sponsor)
	sFinance.save()

	managerGroup = Group.objects.get(name="manager")
	managerGroup.user_set.add(manager)

	drinkGroup = Group.objects.get(name="drink_meister")
	drinkGroup.user_set.add(drinkster)

	sponsorGroup = Group.objects.get(name="sponsor")
	sponsorGroup.user_set.add(sponsor)

	playerGroup = Group.objects.get(name="player")
	playerGroup.user_set.add(manager)
	playerGroup.user_set.add(drinkster)
	playerGroup.user_set.add(sponsor)

	newLogo = SponsorLogo(sponsor=sponsor, logo="logos/mcdonalds.png")
	newLogo.save()

class Migration(migrations.Migration):

	dependencies = [
		('api', '0011_participant'),
	]

	operations = [
		migrations.RunPython(populate_db)
	]