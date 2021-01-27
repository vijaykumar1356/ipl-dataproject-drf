from django.db import models


class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    toss_winner = models.CharField(max_length=100)
    toss_decision = models.CharField(max_length=50)
    winner = models.CharField(max_length=100)
    umpire1 = models.CharField(max_length=100)
    umpire2 = models.CharField(max_length=100)

    class Meta:
        db_table = "matches"

    def __str__(self):
        return f"<Match(id: {self.id}, \
                season: {self.season}, team1: {self.team1}, \
                team2: {self.team2}, winner: {self.winner})>"


class Delivery(models.Model):
    match_id = models.IntegerField()
    batting_team = models.CharField(max_length=200)
    bowling_team = models.CharField(max_length=200)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=120)
    non_striker = models.CharField(max_length=120)
    bowler = models.CharField(max_length=120)
    batsman_runs = models.IntegerField()
    total_runs = models.IntegerField()

    class Meta:
        db_table = "deliveries"

    def __str__(self):
        return f"<Delivery(\
            match_id: {self.match_id}, \
            bat_team: {self.batting_team}, \
            bowl_team: {self.bowling_team}, \
            over: {self.over}, ball: {self.ball}, \
            batsman: {self.batsman}, \
            batsman_runs: {self.batsman_runs}, \
            total_runs: {self.total_runs})>"


class Umpire(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    class Meta:
        db_table = 'umpires'

    def __str__(self):
        return f"<Umpire(name: {self.name}, nationality: {self.nationality})>"
