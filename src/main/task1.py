# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       task1
   Description:
   Author:     bowen
   date:        3/11/19
-------------------------------------------------
"""
from utils.html_util import *
from utils.time_util import get_current_time
from bs4 import BeautifulSoup
from path_config import data_dir
import os
import csv
from utils.team_name_util import team_name_dict


def write_dict(player_dict, dict_fpath):
    with open(dict_fpath, 'a+') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for player in player_dict.values():
            # 'Year', 'Team', 'Team Abbreviation', 'Player'
            row = [player.year, player.team, team_name_dict[player.team], player.name]
            # 'Free Agent', 'Free Agent Date'
            if player.free_agency_date is not None:
                row.extend([1, player.free_agency_date])
            else:
                row.extend(['', ''])
            # 'Team Options Exercised', 'Team Options Exercised Date'
            if player.team_options_exercised is not None:
                row.extend([1, player.team_options_exercised])
            else:
                row.extend(['', ''])
            # 'Veteran Scale Extension', 'Veteran Scale Extension Team', 'Veteran Scale Extension Team Abbreviation'
            if player.veteran_scale_extension is not None:
                row.extend([1, player.veteran_scale_extension, team_name_dict[player.veteran_scale_extension]])
            else:
                row.extend(['', '', ''])
            # 'Rookie Scale Extension', 'Rookie Scale Extension Team', 'Rookie Scale Extension Team Abbreviation'
            if player.rookie_scale_extension is not None:
                row.extend([1, player.rookie_scale_extension, team_name_dict[player.rookie_scale_extension]])
            else:
                row.extend(['', '', ''])
            # 'Waived', 'Waived Date'
            if player.players_waived is not None:
                row.extend([1, player.players_waived])
            else:
                row.extend(['', ''])
            # 'Newly Acquired', 'Newly Acquired Date'
            if player.trade_acquisitions is not None:
                row.extend([1, player.trade_acquisitions])
            else:
                row.extend(['', ''])
            # url
            row.append(player.url)
            writer.writerow(row)


dict_fpath = os.path.join(data_dir, 'task1.csv')

header = ['Year', 'Team', 'Team Abbreviation', 'Player', 'Free Agent', 'Free Agent Date', 'Team Options Exercised',
          'Team Options Exercised Date', 'Veteran Scale Extension', 'Veteran Scale Extension Team',
          'Veteran Scale Extension Team Abbreviation', 'Rookie Scale Extension', 'Rookie Scale Extension Team',
          'Rookie Scale Extension Team Abbreviation', 'Waived', 'Waived Date', 'Newly Acquired',
          'Newly Acquired Date', 'url']

# write header
with open(dict_fpath, 'w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)

cnt = 0
for year in range(1984, 2020, 1):
    for team_id in range(0, 50, 1):

        cnt += 1
        print("# cnt = %s" % cnt)
        # if cnt < 1480:
        #     continue

        player_dict = dict()

        url = 'https://basketball.realgm.com/nba/teams/Random/%s/Transaction_History/%s' % (team_id, year)
        # url = 'https://basketball.realgm.com/nba/teams/Oklahoma-City-Thunder/33/Transaction_History/2017'
        print("Current url %s..." % url, get_current_time())
        html_content = get_html(url)

        if 'err404' in html_content:
            print("url %s 404 error!" % url, get_current_time())
            continue

        soup = BeautifulSoup(html_content, "html.parser")

        season_year, team_name = get_team_info(soup)

        # 1. free_agency
        player_dict = get_free_agency(soup, season_year, team_name, player_dict, url)
        # 2. team_options_exercised
        player_dict = get_team_options_exercised(soup, season_year, team_name, player_dict, url)
        # 3. Veteran Scale Extension
        player_dict = get_veteran_scale_extension(soup, season_year, team_name, player_dict, url)
        # 4. Rookie Scale Extension
        player_dict = get_rookie_scale_extension(soup, season_year, team_name, player_dict, url)
        # 5. trade_acquisitions
        player_dict = get_trade_acquisitions(soup, season_year, team_name, player_dict, url)
        # 6. players_waived
        player_dict = get_players_waived(soup, season_year, team_name, player_dict, url)

        write_dict(player_dict, dict_fpath)
