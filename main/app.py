from lib.Driver import Driver
from pages.fantasydata.GameStats import GameStats

import json

driver = Driver(headless=False)

season = 2020
weeks = [1, 2, 3, 4, 5]
player_scores = {}

for week in weeks:
    game_stats = GameStats(driver, season=season, startweek=week, endweek=week)

    game_stats.set_players_displayed(300)
    names = game_stats.get_names_displayed()
    scores = game_stats.get_scores_displayed()
    ids = game_stats.get_ids_displayed()

    count = 0

    while count < len(names):
        player = player_scores.get(names[count])

        if not player:
            player = {}

        key = f'week_{week}_score'
        player[key] = scores[count]
        player['fantasydata_id'] = ids[count]
        player_scores[names[count]] = player
        count += 1

with open('data.json', 'w+') as f:
    score_objs = []
    for player in player_scores:
        score_obj = player_scores[player]
        score_obj['name'] = player
        score_objs.append(score_obj)


    f.write(json.dumps(score_objs))

driver.close()