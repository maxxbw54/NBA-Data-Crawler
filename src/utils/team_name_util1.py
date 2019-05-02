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
    'BRK': 'Brooklyn Nets',
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
    'PHI': 'Philadelphia Sixers',
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
    'CB': 'Charlotte Bobcats',
    'BRK': 'Brooklyn Nets',
    'SEA': 'Seattle SuperSonics',
    'VAN': 'Vancouver Grizzlies'
}

team_name_dict = dict()
for k, v in name_dict_one_side.items():
    team_name_dict[k] = v
    team_name_dict[v] = k

target_name_dict_one_side = {
    'ATL': 'Atlanta Hawks',
    'BRK': 'Brooklyn Nets',
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
    'PHI': 'Philadelphia Sixers',
    'PHX': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards',
    # added later
    # 'TCB': 'Tri-Cities Blackhawks',
    # 'PW': 'Philadelphia Warriors',
    # 'MH': 'Milwaukee Hawks',
    # 'SLH': 'St. Louis Hawks',
    # 'BB': 'Buffalo Braves',
    'NJN': 'New Jersey Nets',
    'PHI': 'Philadelphia Sixers',
    # 'SS': 'Seattle SuperSonics',
    # 'WB': 'Washington Bullets',
    # 'KCK': 'Kansas City Kings',
    # 'SDC': 'San Diego Clippers',
    # 'NOJ': 'New Orleans Jazz',
    # 'SDR': 'San Diego Rockets',
    # 'CR': 'Cincinnati Royals',
    # 'NYN': 'New York Nets',
    # 'ML': 'Minneapolis Lakers',
    # 'CZ': 'Chicago Zephyrs',
    # 'CH88': 'Charlotte Hornets (1988)',
    # 'VG': 'Vancouver Grizzlies',
    # 'NOH': 'New Orleans Hornets',
    # 'CB': 'Charlotte Bobcats'
}

target_team_name_dict = dict()
for k, v in target_name_dict_one_side.items():
    target_team_name_dict[k] = v
    target_team_name_dict[v] = k

target_full_to_abbr_dict = {
    'Atlanta Hawks': ['ATL'],
    'Brooklyn Nets': ['BRK', 'NJN'],
    'Boston Celtics': ['BOS'],
    'Charlotte Hornets': ['CHA'],
    'Chicago Bulls': ['CHI'],
    'Cleveland Cavaliers': ['CLE'],
    'Dallas Mavericks': ['DAL'],
    'Denver Nuggets': ['DEN'],
    'Detroit Pistons': ['DET'],
    'Golden State Warriors': ['GSW'],
    'Houston Rockets': ['HOU'],
    'Indiana Pacers': ['IND'],
    'Los Angeles Clippers': ['LAC', 'SDC'],
    'Los Angeles Lakers': ['LAL'],
    'Memphis Grizzlies': ['MEM', 'VAN'],
    'Miami Heat': ['MIA'],
    'Milwaukee Bucks': ['MIL'],
    'Minnesota Timberwolves': ['MIN'],
    'New Orleans Pelicans': ['NOP', 'CHA'],
    'New York Knicks': ['NYK'],
    'Oklahoma City Thunder': ['OKC', 'SEA'],
    'Orlando Magic': ['ORL'],
    'Philadelphia Sixers': ['PHI'],
    'Phoenix Suns': ['PHX'],
    'Portland Trail Blazers': ['POR'],
    'Sacramento Kings': ['SAC', 'KCK'],
    'San Antonio Spurs': ['SAS'],
    'Toronto Raptors': ['TOR'],
    'Utah Jazz': ['UTA'],
    'Washington Wizards': ['WAS'],
    'New Jersey Nets': ['BRK', 'NJN'],
    # 'Philadelphia Sixers': ['PS']
}
