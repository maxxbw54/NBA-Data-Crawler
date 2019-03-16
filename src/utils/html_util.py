# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       html_utils
   Description:
   Author:     bowen
   date:        3/11/19
-------------------------------------------------
"""
from data_structure.player import Player


def get_html(url):
    import requests
    page = requests.get(url)
    return page.text


def get_free_agency(soup, season_year, team_name, player_dict, url):
    cnt = 0
    for info in soup.findAll("div", {"class": "portal widget"}):
        if info.text.strip().startswith('Players Becoming Free Agents'):
            for fa in info.findAll('p'):
                date = fa.text.strip().split('\n')[0].strip()
                player_name = fa.text.strip().split('\n')[1].strip()
                if player_name in player_dict:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)].free_agency_date = date
                else:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)] = Player(name=player_name,
                                                                                             year=season_year,
                                                                                             team=team_name,
                                                                                             free_agency_date=date,
                                                                                             url=url)
                cnt += 1
            break
    print("# free agency player %s" % cnt)
    return player_dict


def get_team_options_exercised(soup, season_year, team_name, player_dict, url):
    cnt = 0
    for info in soup.findAll("div", {"class": "portal widget"}):
        if info.text.strip().startswith('Team Options Exercised'):
            for fa in info.findAll('p'):
                date = fa.text.strip().split('\n')[0].strip()
                player_name = fa.text.strip().split('\n')[1].strip()
                if player_name in player_dict:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)].team_options_exercised = date
                else:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)] = Player(name=player_name,
                                                                                             year=season_year,
                                                                                             team=team_name,
                                                                                             team_options_exercised=date,
                                                                                             url=url)
                cnt += 1
            break
    print("# Team Options Exercised %s" % cnt)
    return player_dict


def get_trade_acquisitions(soup, season_year, team_name, player_dict, url):
    cnt = 0
    for info in soup.findAll("div", {"class": "portal widget"}):
        if info.text.strip().startswith('Trade Acquisitions'):
            for fa in info.findAll('p'):
                date = fa.text.strip().split('\n')[0].strip()
                player_name = fa.text.strip().split('\n')[1].strip()
                if player_name in player_dict:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)].trade_acquisitions = date
                else:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)] = Player(name=player_name,
                                                                                             year=season_year,
                                                                                             team=team_name,
                                                                                             trade_acquisitions=date,
                                                                                             url=url)
                cnt += 1
            break
    print("# Trade Acquisitions %s" % cnt)
    return player_dict


def get_players_waived(soup, season_year, team_name, player_dict, url):
    cnt = 0
    for info in soup.findAll("div", {"class": "portal widget"}):
        if info.text.strip().startswith('Players Waived'):
            for fa in info.findAll('p'):
                date = fa.text.strip().split('\n')[0].strip()
                player_name = fa.text.strip().split('\n')[1].strip()
                if player_name in player_dict:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)].players_waived = date
                else:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)] = Player(name=player_name,
                                                                                             year=season_year,
                                                                                             team=team_name,
                                                                                             players_waived=date,
                                                                                             url=url)
                cnt += 1
            break
    print("# Players Waived %s" % cnt)
    return player_dict


def get_veteran_scale_extension(soup, season_year, team_name, player_dict, url):
    cnt = 0
    for info in soup.findAll("div", {"class": "portal widget fullpage"}):
        for fa in info.findAll('li'):
            if 'signed a veteran extension with the' in fa.text:
                player_name = fa.text.strip().split('signed a veteran extension with the')[0].strip()
                veteran_team_name = fa.text.strip().split('signed a veteran extension with the')[1] \
                    .replace('.', '').strip()
                if player_name in player_dict:
                    player_dict[
                        '%s-%s-%s' % (season_year, team_name, player_name)].veteran_scale_extension = veteran_team_name
                else:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)] = Player(name=player_name,
                                                                                             year=season_year,
                                                                                             team=team_name,
                                                                                             veteran_scale_extension=veteran_team_name,
                                                                                             url=url)
                cnt += 1
    print("# Veteran Scale Extension %s" % cnt)
    return player_dict


def get_rookie_scale_extension(soup, season_year, team_name, player_dict, url):
    cnt = 0
    for info in soup.findAll("div", {"class": "portal widget fullpage"}):
        for fa in info.findAll('li'):
            if 'signed a rookie scale extension with the' in fa.text:
                player_name = fa.text.strip().split('signed a rookie scale extension with the')[0].strip()
                rookie_scale_extension_team_name = fa.text.strip().split('signed a rookie scale extension with the')[
                    1].replace('.', '').strip()
                if player_name in player_dict:
                    player_dict['%s-%s-%s' % (
                        season_year, team_name, player_name)].rookie_scale_extension = rookie_scale_extension_team_name
                else:
                    player_dict['%s-%s-%s' % (season_year, team_name, player_name)] = Player(name=player_name,
                                                                                             year=season_year,
                                                                                             team=team_name,
                                                                                             rookie_scale_extension=rookie_scale_extension_team_name,
                                                                                             url=url)
                cnt += 1
    print("# Rookie Scale Extension %s" % cnt)
    return player_dict


def get_team_info(soup):
    for title in soup.findAll("h2", {"class": "page_title"}):
        if 'Transactions History' in title.text:
            text = title.text.replace('Transactions History', '').strip()
            team_name = ' '.join(text.split()[1:])
            season_year = text.split()[0]
            break
    print("Season %s, Team %s" % (season_year, team_name))
    return season_year, team_name
