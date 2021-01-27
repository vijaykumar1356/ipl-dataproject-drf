
from django.db.models import (Count, Sum)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Delivery, Match, Umpire
from app.api.serializers import (
    Problem1Serializer,
    Problem2Serializer,
    Problem3Serializer,
    Problem4Serializer1,
    Problem4Serializer2
)


@api_view(['GET'])
def problem1_api(request):
    parameters = dict(request.query_params)
    if parameters:
        teams_dict = {
            'mi': 'Mumbai Indians',
            'rcb': 'Royal Challengers Bangalore',
            'kxip':  'Kings XI Punjab',
            'dd': 'Delhi Daredevils',
            'csk': 'Chennai Super Kings',
            'rr': 'Rajasthan Royals',
            'srh': 'Sunrisers Hyderabad',
            'pw': 'Pune Warriors',
            'gl': 'Gujarat Lions',
            'rps': 'Rising Pune Supergiants',
            'ktk':  'Kochi Tuskers Kerala',
            'kkr': 'Kolkata Knight Riders'
        }

        years = sorted(
            [int(parameters['start'][0]), int(parameters['end'][0])]
            )
        match_ids = []
        for year in range(years[0], years[1]+1):
            m_ids = Match.objects.values('id').filter(season=year)
            for obj in m_ids:
                match_ids.append(obj['id'])
        teams = parameters['teams']

        filtered_teams = []
        for team in teams:
            filtered_teams.append(teams_dict[team])

        objects = Delivery.objects.values('batting_team')\
            .filter(match_id__in=match_ids)\
            .filter(batting_team__in=filtered_teams)\
            .annotate(sum_score=Sum("total_runs")).order_by('-sum_score')

        serializer = Problem1Serializer(objects, many=True)
        return Response(serializer.data)

    else:
        objects = Delivery.objects.values('batting_team')\
                .annotate(sum_score=Sum("total_runs")).order_by('-sum_score')
        serializer = Problem1Serializer(objects, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def problem2_api(request):
    teams_dict = {
            'mi': 'Mumbai Indians',
            'rcb': 'Royal Challengers Bangalore',
            'kxip':  'Kings XI Punjab',
            'dd': 'Delhi Daredevils',
            'csk': 'Chennai Super Kings',
            'rr': 'Rajasthan Royals',
            'srh': 'Sunrisers Hyderabad',
            'pw': 'Pune Warriors',
            'gl': 'Gujarat Lions',
            'rps': 'Rising Pune Supergiants',
            'ktk':  'Kochi Tuskers Kerala',
            'kkr': 'Kolkata Knight Riders'
        }
    parameters = request.query_params
    if parameters:
        year = parameters['year']
        match_ids = []
        top = parameters['top']
        m_ids = Match.objects.values('id').filter(season=year)
        for obj in m_ids:
            match_ids.append(obj['id'])
        team = parameters['team']
        filtered_team = teams_dict[team]
        objects = Delivery.objects.values('batsman')\
            .filter(batting_team=filtered_team)\
            .filter(match_id__in=match_ids)\
            .annotate(total_runs=Sum('batsman_runs'))\
            .order_by('-total_runs')[:int(top)]
        serializer = Problem2Serializer(objects, many=True)
        return Response(serializer.data)
    else:
        objects = Delivery.objects.values('batting_team', 'batsman')\
            .filter(batting_team='Pune Warriors')\
            .annotate(total_runs=Sum('batsman_runs'))\
            .order_by('-total_runs')[:10]
        serializer = Problem2Serializer(objects, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def problem3_api(request):
    parameters = dict(request.query_params)
    if parameters:
        country_dict = {
            'ind': 'India', 'aus': 'Australia',
            'sa': 'South Africa', 'eng': 'England',
            'nz': 'New Zealand', 'sl': 'Sri Lanka',
            'pak': 'Pakistan', 'wi': 'West Indies',
            'zim': 'Zimbabwe'
        }
        filtered_countries = []
        for country in parameters['countries']:
            filtered_countries.append(country_dict[country])
        objects = Umpire.objects.values('nationality')\
            .filter(nationality__in=filtered_countries)\
            .annotate(umpire_count=Count('nationality'))\
            .order_by('-umpire_count')
        serializer = Problem3Serializer(objects, many=True)
        countries = []
        count = []
        for obj in serializer.data:
            countries.append(obj['nationality'])
            count.append(obj['umpire_count'])
        return Response({'countries': countries, 'count': count})
    else:
        objects = Umpire.objects.values('nationality')\
            .annotate(umpire_count=Count("nationality"))\
            .order_by('-umpire_count')
        serializer = Problem3Serializer(objects, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def problem4_api(request):
    parameters = dict(request.query_params)
    teams_dict = {
        'mi': 'Mumbai Indians',
        'rcb': 'Royal Challengers Bangalore',
        'kxip':  'Kings XI Punjab',
        'dd': 'Delhi Daredevils',
        'csk': 'Chennai Super Kings',
        'rr': 'Rajasthan Royals',
        'srh': 'Sunrisers Hyderabad',
        'pw': 'Pune Warriors',
        'gl': 'Gujarat Lions',
        'rps': 'Rising Pune Supergiants',
        'ktk':  'Kochi Tuskers Kerala',
        'kkr': 'Kolkata Knight Riders'
        }

    if parameters:
        years_range = sorted(
            [int(parameters['start'][0]), int(parameters['end'][0])]
            )
        years = [year for year in range(years_range[0], years_range[1]+1)]
        teams = [teams_dict[team] for team in parameters['teams']]

        objects_1 = Match.objects.values('season', 'team1')\
            .filter(team1__in=teams)\
            .filter(season__in=years)\
            .annotate(team1_count=Count('team1'))\
            .order_by('-team1_count')

        objects_2 = Match.objects.values('season', 'team2')\
            .filter(team2__in=teams)\
            .filter(season__in=years)\
            .annotate(team2_count=Count('team2'))\
            .order_by('-team2_count')

        serializer_1 = Problem4Serializer1(objects_1, many=True)
        serializer_2 = Problem4Serializer2(objects_2, many=True)
        season_data = {}
        for year in years:
            season_data.setdefault(year, {})
            for team in teams:
                season_data[year].setdefault(team, 0)
        for obj in serializer_1.data:
            season_data[obj['season']][obj['team1']] += obj['team1_count']
        for obj in serializer_2.data:
            season_data[obj['season']][obj['team2']] += obj['team2_count']
        season_wise_matches = []
        uniq_teams = list(season_data[years[0]].keys())
        for key in season_data:
            season_wise_matches.append(list(season_data[key].values()))
        return Response({
            "years": years,
            "teams": uniq_teams,
            "matches_played": season_wise_matches
            })
    else:
        objects_1 = Match.objects.values('season', 'team1')\
            .annotate(team1_count=Count('team1'))\
            .order_by('season', '-team1_count')

        objects_2 = Match.objects.values('season', 'team2')\
            .annotate(team2_count=Count('team2'))\
            .order_by('season', '-team2_count')
        serializer_1 = Problem4Serializer1(objects_1, many=True)
        serializer_2 = Problem4Serializer2(objects_2, many=True)
        serializer = serializer_1.data + serializer_2.data
        season_data = {}
        for obj in serializer:
            season_data.setdefault(obj['season'], {})
            if "team1" in obj.keys():
                season_data[obj['season']].setdefault(obj['team1'], 0)
                season_data[obj['season']][obj['team1']] += obj['team1_count']
            else:
                season_data[obj['season']].setdefault(obj['team2'], 0)
                season_data[obj['season']][obj['team2']] += obj['team2_count']
        uniq_teams = set()
        for key in season_data:
            teams = set(season_data[key].keys())
            uniq_teams.update(teams)
        for key in season_data:
            for team in uniq_teams:
                if team not in season_data[key].keys():
                    season_data[key].setdefault(team, 0)
            season_data[key] = dict(
                    sorted(season_data[key].items(), key=lambda x: x[0])
                    )
        return Response(season_data)
