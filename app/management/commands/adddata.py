from django.core.management.base import BaseCommand, CommandError
from app.models import Delivery, Match, Umpire
import os
import csv

class Command(BaseCommand):
    help = "Loading 'deliveries.csv', 'matches.csv' files to Postgres database 'djangoproject'"
    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        if os.path.exists('deliveries.csv') and os.path.exists('matches.csv') and os.path.exists('umpires.csv'):
            
            with open('matches.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                matches = []
                for row in csv_reader:
                    matches.append(Match(
                            id=row['id'],
                            season=row['season'],
                            team1=row['team1'], 
                            team2=row['team2'],
                            toss_winner=row['toss_winner'],
                            toss_decision=row['toss_decision'],
                            winner=row['winner'],
                            umpire1=row['umpire1'],
                            umpire2=row['umpire2'],
                            ))
                Match.objects.bulk_create(matches, batch_size=None, ignore_conflicts=False)

            with open('deliveries.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                deliveries = []
                for row in csv_reader:
                    deliveries.append(Delivery(
                                match_id=row['match_id'],
                                batting_team=row['batting_team'],
                                bowling_team=row['bowling_team'], 
                                over=row['over'],
                                ball=row['ball'],
                                batsman=row['batsman'],
                                non_striker=row['non_striker'],
                                bowler=row['bowler'],
                                batsman_runs=row['batsman_runs'],
                                total_runs=row['total_runs']
                                ))
                Delivery.objects.bulk_create(deliveries, batch_size=None, ignore_conflicts=False)


            with open('umpires.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                umpires = []
                for row in csv_reader:
                    umpires.append(Umpire(
                        name=row['umpire'],
                        nationality=row['nationality']
                     ))
                Umpire.objects.bulk_create(umpires, batch_size=None, ignore_conflicts=False)
            self.stdout.write(self.style.SUCCESS("Data loaded to database successfully!"))

            
        else:
            raise CommandError("one or more of csv files in ['deliveries.csv', 'matches.csv', 'umpires.csv'] are missing in project directory! ")
