# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       task2
   Description:
   Author:     bowen
   date:        3/11/19
-------------------------------------------------
"""
from utils.html_util_task2 import *
from utils.time_util import get_current_time
from bs4 import BeautifulSoup
from path_config import data_dir
import os
import csv
from utils.team_name_util import team_name_dict, target_team_name_dict


def write_dict(player_dict, dict_fpath):
    with open(dict_fpath, 'a+') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for player in player_dict.values():
            # 'Year', 'Team', 'Team Abbreviation', 'Player'
            if player.team not in target_team_name_dict:
                continue
            row = [player.year, player.team, target_team_name_dict[player.team], player.name]
            # 'Traded Date', 'Traded Team'
            if player.traded_team is not None:
                row.extend([player.traded_date, player.traded_team])
            else:
                row.extend(['', ''])
            # 'Free Agent', 'Free Agent Date'
            if player.free_agency_date is not None:
                row.extend([1, player.free_agency_date])
            else:
                row.extend(['', ''])
            # 'Waived', 'Waived Date'
            if player.players_waived is not None:
                row.extend([1, player.players_waived])
            else:
                row.extend(['', ''])
            # 'Destination Team', 'Destination Team Abbreviation'
            if player.destination_team is not None:
                if player.destination_team not in target_team_name_dict:
                    continue
                row.extend([player.destination_team, team_name_dict[player.destination_team]])
            else:
                row.extend(['', ''])
            # 'Sign Contract', 'Sign Contract Date'
            if player.sign_contract_date is not None:
                row.extend([1, player.sign_contract_date])
            else:
                row.extend(['', ''])
            # type
            row.append(player.type)
            # url
            row.append(player.url)
            writer.writerow(row)


dict_fpath = os.path.join(data_dir, 'task2.csv')

header = ['Year', 'Team', 'Team Abbreviation', 'Player', 'Traded Date', 'Traded Team', 'Free Agent', 'Free Agent Date',
          'Waived', 'Waived Date',
          'Destination Team Abbreviation', 'Destination Team', 'Sign Contract', 'Sign Contract Date', 'Type', 'url']

# write header
with open(dict_fpath, 'w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)

cnt = 0
for team_id in range(0, 50, 1):

    cnt += 1
    print("# cnt = %s" % cnt)

    url = 'https://basketball.realgm.com/nba/teams/random/%s/roster-turnover' % team_id
    # url = 'https://basketball.realgm.com/nba/teams/Oklahoma-City-Thunder/33/roster-turnover'
    print("Current url %s..." % url, get_current_time())
    html_content = get_html(url)

    if 'err404' in html_content:
        print("url %s 404 error!" % url, get_current_time())
        continue

    team_name = get_team_info(BeautifulSoup(html_content, "html.parser"))

    if team_name not in target_team_name_dict:
        continue

    year_html_content_list = html_content.split('<div style="clear: both;"></div>')

    for year_html_content in year_html_content_list:
        player_dict = dict()
        if '<h2 class="clearfix" style="line-height: 42px;">' in year_html_content:
            idx = year_html_content.index('<h2 class="clearfix" style="line-height: 42px;">')
            year_html_content = year_html_content[idx:]
            year_soup = BeautifulSoup(year_html_content, "html.parser")
            season_year = get_season_year(year_soup, team_name)
            for table_soup in year_soup.findAll("table"):
                if '<th class="nosort" colspan="3">Lost</th>' in str(table_soup):
                    player_dict = get_lost(table_soup, season_year, team_name, player_dict, url)
                    write_dict(player_dict, dict_fpath)
                    player_dict = dict()
                elif '<th class="nosort" colspan="3">Added</th>' in str(table_soup):
                    player_dict = get_added(table_soup, season_year, team_name, player_dict, url)
                    write_dict(player_dict, dict_fpath)
                    player_dict = dict()
            print("Finished year %s" % season_year)
