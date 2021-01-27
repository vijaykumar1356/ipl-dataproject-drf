from rest_framework import serializers


class Problem1Serializer(serializers.Serializer):
    batting_team = serializers.CharField(max_length=200)
    sum_score = serializers.IntegerField()


class Problem2Serializer(serializers.Serializer):
    batsman = serializers.CharField(max_length=200)
    total_runs = serializers.IntegerField()


class Problem3Serializer(serializers.Serializer):
    nationality = serializers.CharField(max_length=100)
    umpire_count = serializers.IntegerField()


class Problem4Serializer1(serializers.Serializer):
    season = serializers.IntegerField()
    team1 = serializers.CharField(max_length=100)
    team1_count = serializers.IntegerField()


class Problem4Serializer2(serializers.Serializer):
    season = serializers.IntegerField()
    team2 = serializers.CharField(max_length=100)
    team2_count = serializers.IntegerField()
