# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       team_name_util
   Description:
   Author:     bowen
   date:        3/16/19
-------------------------------------------------
"""

name_dict_one_side = {
    'ATL': 'Atlanta Hawks',
    'BKN': 'Brooklyn Nets',
    'BOS': 'Boston Celtics',
    'CHA': 'Charlotte Hornets',
    'CHI': 'Chicago Bulls',
    'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors',
    'HOU': 'Houston Rockets',
    'IND': 'Indiana Pacers',
    'LAC': 'Los Angeles Clippers',
    'LAL': 'Los Angeles Lakers',
    'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks',
    'MIN': 'Minnesota Timberwolves',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHX': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards',
    # added later
    'TCB': 'Tri-Cities Blackhawks',
    'PW': 'Philadelphia Warriors',
    'MH': 'Milwaukee Hawks',
    'SLH': 'St. Louis Hawks',
    'BB': 'Buffalo Braves',
    'NJN': 'New Jersey Nets',
    'PS': 'Philadelphia Sixers',
    'SS': 'Seattle SuperSonics',
    'WB': 'Washington Bullets',
    'KCK': 'Kansas City Kings',
    'SDC': 'San Diego Clippers',
    'NOJ': 'New Orleans Jazz',
    'SDR': 'San Diego Rockets',
    'CR': 'Cincinnati Royals',
    'NYN': 'New York Nets',
    'ML': 'Minneapolis Lakers',
    'CZ': 'Chicago Zephyrs',
    'CH88': 'Charlotte Hornets (1988)',
    'VG': 'Vancouver Grizzlies',
    'NOH': 'New Orleans Hornets',
    'CB': 'Charlotte Bobcats'
}

team_name_dict = dict()
for k, v in name_dict_one_side.items():
    team_name_dict[k] = v
    team_name_dict[v] = k
