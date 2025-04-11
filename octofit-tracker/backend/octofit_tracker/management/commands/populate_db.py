from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create(email='user1@example.com', name='User One')
        user2 = User.objects.create(email='user2@example.com', name='User Two')
        user3 = User.objects.create(email='user3@example.com', name='User Three')

        # Create teams with user emails
        team1 = Team.objects.create(name='Team Alpha', members=[user1.email, user2.email])
        team2 = Team.objects.create(name='Team Beta', members=[user3.email])

        # Create activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-10')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-09')

        # Create leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=80)

        # Create workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session', duration=60)
        Workout.objects.create(name='HIIT', description='High-intensity interval training', duration=30)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
