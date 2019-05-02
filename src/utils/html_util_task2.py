# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       html_utils
   Description:
   Author:     bowen
   date:        3/11/19
-------------------------------------------------
"""
from data_structure.player2 import Player


def get_html(url):
    import requests
    page = requests.get(url)
    return page.text


def get_season_year(year_soup, team_name):
    for h2 in year_soup.findAll("h2"):
        season_year = h2.text.replace(team_name, '').replace('Roster Turnover', '').strip()
        return season_year.split(' to ')[0].split('-')[1]


def get_lost(table_soup, season_year, team_name, player_dict, url):
    from utils.team_name_util2 import target_full_to_abbr_dict
    cnt = 0
    for td in table_soup.findAll("td"):
        player_name = None
        free_agent_date = None
        destination_team = None
        waived_date = None
        traded_date = None
        traded_team = None
        if_valid = False
        for a in td.findAll("a", {"style": "font-weight: bold; text-decoration: none;"}):
            player_name = a.text
            break

        if player_name is None:
            continue

        for li in td.findAll("li"):
            s = li.text
            if 'Free Agent' in s and any(team_name_abbr in s for team_name_abbr in target_full_to_abbr_dict[team_name]):
                free_agent_date = s.split(' on ')[1].strip()
                if_valid = True
            if 'Signed Contract' in s and any(
                    team_name_abbr in s for team_name_abbr in target_full_to_abbr_dict[team_name]):
                if ' to ' in s:
                    destination_team = s[s.find("(") + 1:s.find(")")].split(' to ')[1].strip()
                    if_valid = True
                else:
                    destination_team = s[s.find("(") + 1:s.find(")")].strip()
                    if_valid = True
            if 'Waived' in s and any(team_name_abbr in s for team_name_abbr in target_full_to_abbr_dict[team_name]):
                waived_date = s.split(' on ')[1].strip()
                if_valid = True
            if 'Traded' in s and any(team_name_abbr in s for team_name_abbr in target_full_to_abbr_dict[team_name]):
                traded_date = s.split(' on ')[1].strip()
                traded_team = s[s.find("(") + 1:s.find(")")].split('to')[1].strip()
                if_valid = True
        if if_valid:
            player_dict[player_name] = Player(name=player_name, year=season_year, team=team_name,
                                              free_agency_date=free_agent_date, destination_team=destination_team,
                                              players_waived=waived_date, traded_date=traded_date,
                                              traded_team=traded_team,
                                              url=url, type='Lost')
        cnt += 1
    # print("# lost %s" % cnt)
    return player_dict


def get_added(table_soup, season_year, team_name, player_dict, url):
    cnt = 0
    for td in table_soup.findAll("td"):
        player_name = None
        destination_team = None
        sign_contract_date = None
        traded_date = None
        traded_team = None
        if_valid = False
        for a in td.findAll("a", {"style": "font-weight: bold; text-decoration: none;"}):
            player_name = a.text

        if player_name is None:
            continue
        for li in td.findAll("li"):
            s = li.text
            if 'Signed Contract' in s:
                sign_contract_date = s.split(' on ')[1].strip()
                if_valid = True
            if 'Traded' in s:
                if_valid = True
        if if_valid:
            player_dict[player_name] = Player(name=player_name, year=season_year, team=team_name,
                                              sign_contract_date=sign_contract_date, destination_team=destination_team,
                                              traded_date=traded_date, traded_team=traded_team, url=url, type='Added')
        cnt += 1
    # print("# added %s" % cnt)
    return player_dict


def get_team_info(soup):
    for title in soup.findAll("h2", {"class": "page_title"}):
        if 'Roster Turnover' in title.text:
            team_name = title.text.replace('Roster Turnover', '').strip()
            break
    print("Team %s" % team_name)
    return team_name
