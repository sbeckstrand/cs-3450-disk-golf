from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Tournament, Drink, DrinkOrder
  
class TournamentTest(TestCase):

    def create_tournament(self, name="Test Case Tournament", description="Test Case Description", holes=18, participants=10, startDate="2021-10-1 12:00:00+00:00"):
        return Tournament.objects.create(name=name, description=description, holes=holes, participants=participants, startDate=startDate)

    def test_tournament_creation(self):
        t = self.create_tournament()
        print("\nTesting Tournament Creation: ", end="")
        try:
            self.assertTrue(isinstance(t, Tournament))
            print("Pass")

        except:
            print("Fail")

    def test_tournament_url(self):
        response = self.client.get("/api/tournaments")
        print("\nTesting Tournament /api/tournaments endpoint: ", end="")
        try:
            self.assertEqual(response.status_code, 301)
            print("Pass")
        except:
            print("Fail")

class DrinkTest(TestCase):

    def create_drink(self, name="Test Case Drink", description="Test Case Description", type="hard", price=10):
        return Drink.objects.create(name=name, description=description, type=type, price=price)

    def test_drink_creation(self):
        d = self.create_drink()
        print("\nTesting Drink Creation: ", end="")
        try:
            self.assertTrue(isinstance(d, Drink))
            print("Pass")

        except:
            print("Fail")

    def test_drink_url(self):
        response = self.client.get("/api/drinks")
        print("\nTesting Drink /api/drinks endpoint: ", end="")
        try:
            self.assertEqual(response.status_code, 301)
            print("Pass")
        except:
            print("Fail")

class UserTest(TestCase):

    def create_user(self, username="testuser", email="test@test.com", password="testPassword"):
        return User.objects.create(username=username, email=email, password=password)

    def test_user_creation(self):
        u = self.create_user()
        print("\nTesting User Creation: ", end="")
        try:
            self.assertTrue(isinstance(u, User))
            print("Pass")

        except:
            print("Fail")

    def test_users_url(self):
        response = self.client.get("/api/users")
        print("\nTesting User /api/users endpoint: ", end="")
        try:
            self.assertEqual(response.status_code, 301)
            print("Pass")
        except:
            print("Fail")


class DrinkOrderTest(TestCase):

    def create_drink_order(self):
        user = User.objects.create(username="drinkuser", email="user@drink.com", password="drinkpassword")
        drink = Drink.objects.create(name="order drink", description="Drink for test order", type="soft", price=100)
        return DrinkOrder.objects.create(drink=drink, client=user)

    def test_drink_order_creation(self):
        do = self.create_drink_order()
        print("\nTesting Drink Order Creation: ", end="")
        try:
            self.assertTrue(isinstance(do, DrinkOrder))
            print("Pass")

        except:
            print("Fail")

    def test_drink_order_url(self):
        response = self.client.get("/api/orders")
        print("\nTesting Drink Orders /api/orders endpoint: ", end="")
        try:
            self.assertEqual(response.status_code, 301)
            print("Pass")
        except:
            print("Fail")