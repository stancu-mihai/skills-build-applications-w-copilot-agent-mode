from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(email="test@example.com", name="Test User")

    def test_user_creation(self):
        user = User.objects.get(email="test@example.com")
        self.assertEqual(user.name, "Test User")

# Add similar tests for teams, activity, leaderboard, and workouts.
