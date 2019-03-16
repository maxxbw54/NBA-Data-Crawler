# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       player
   Description:
   Author:     bowen
   date:        3/11/19
-------------------------------------------------
"""


class Player(object):

    def __init__(self, name, year, team, free_agency_date=None, team_options_exercised=None, trade_acquisitions=None,
                 players_waived=None, veteran_scale_extension=None, rookie_scale_extension=None, url=None):
        self.name = name
        self.year = year
        self.team = team
        self.free_agency_date = free_agency_date
        self.team_options_exercised = team_options_exercised
        self.trade_acquisitions = trade_acquisitions
        self.players_waived = players_waived
        self.veteran_scale_extension = veteran_scale_extension
        self.rookie_scale_extension = rookie_scale_extension
        self.url = url
