from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='cap@marvel.com', name='Captain America', team='marvel'),
            User(email='thor@marvel.com', name='Thor', team='marvel'),
            User(email='hulk@marvel.com', name='Hulk', team='marvel'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
            User(email='flash@dc.com', name='Flash', team='dc'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Iron Man', type='run', duration=30, date='2026-03-17'),
            Activity(user='Captain America', type='cycle', duration=45, date='2026-03-17'),
            Activity(user='Thor', type='swim', duration=25, date='2026-03-17'),
            Activity(user='Hulk', type='lift', duration=60, date='2026-03-17'),
            Activity(user='Superman', type='fly', duration=120, date='2026-03-17'),
            Activity(user='Batman', type='run', duration=40, date='2026-03-17'),
            Activity(user='Wonder Woman', type='cycle', duration=50, date='2026-03-17'),
            Activity(user='Flash', type='run', duration=10, date='2026-03-17'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=250)
        Leaderboard.objects.create(team='dc', points=220)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', suggested_for='marvel'),
            Workout(name='Flying', description='Practice flying for 10 minutes', suggested_for='dc'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with superhero test data.'))
