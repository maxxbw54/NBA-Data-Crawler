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

    def __init__(self, name, year, team, free_agency_date=None, sign_contract_date=None, players_waived=None, url=None,
                 traded_date=None, traded_team=None, destination_team=None, type=None):
        self.name = name
        self.year = year
        self.team = team
        self.sign_contract_date = sign_contract_date
        self.free_agency_date = free_agency_date
        self.traded_date = traded_date
        self.traded_team = traded_team
        self.players_waived = players_waived
        self.destination_team = destination_team
        self.url = url
        # added or lost
        self.type = type
