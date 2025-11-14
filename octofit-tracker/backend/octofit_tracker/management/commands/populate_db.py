from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Example: clear and create test data for users, teams, activities, leaderboard, workouts
        # This is a stub. You should implement actual models and logic.
        self.stdout.write(self.style.SUCCESS('Populating octofit_db with test data...'))
        # TODO: Implement actual data population logic here
        self.stdout.write(self.style.SUCCESS('Done populating octofit_db.'))
