from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(str(team), 'Marvel')
    def test_create_user(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(email='batman@dc.com', name='Batman', team=team)
        self.assertEqual(str(user), 'batman@dc.com')
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='spidey@marvel.com', name='Spiderman', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2025-11-14')
        self.assertEqual(activity.type, 'run')
    def test_create_workout(self):
        user = User.objects.create(email='ironman@marvel.com', name='Iron Man')
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout.suggested_for.add(user)
        self.assertEqual(workout.name, 'Pushups')
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)
