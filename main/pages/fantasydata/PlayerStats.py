from lib.Page import Page
import time

class PlayerStats(Page):

    def __init__(self, driver, navigate=True, season=2020, startweek=1, endweek=1):
        url = f'https://fantasydata.com/nfl/fantasy-football-leaders?position=1&season={season}&seasontype=1&scope=2&subscope=1&startweek={startweek}&endweek={endweek}&aggregatescope=1&range=3'

        super().__init__(driver, url, navigate=navigate)