from django.contrib.auth.models import Group

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Create groups necessary for Disk Golf App"

    def handle(self, *args, **options):
        players, created = Group.objects.get_or_create(name="players")
        managers, created = Group.objects.get_or_create(name="mangers")
        drink_meisters, created = Group.objects.get_or_create(name="meisters")
        sponsors, created = Group.objects.get_or_create(name="sponsors")