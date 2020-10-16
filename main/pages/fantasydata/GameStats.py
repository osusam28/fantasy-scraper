from lib.Page import Page
import time

class GameStats(Page):

    def __init__(self, driver, navigate=True, season=2020, startweek=1, endweek=1):
        url = f'https://fantasydata.com/nfl/fantasy-football-leaders?position=1&season={season}&seasontype=1&scope=2&subscope=1&startweek={startweek}&endweek={endweek}&aggregatescope=1&range=3'

        super().__init__(driver, url, navigate=navigate)

    def get_names_displayed(self):
        # wait for javascript table to load
        time.sleep(10)

        table_elements = self.driver.get_elements_by_xpath('/html/body/div[6]/div/div[3]/div[2]/div/div/div[2]/section/div/div[3]/div[3]/div[2]/table/tbody/tr')
        
        names = []
        for table_element in table_elements:
            link = table_element.find_element_by_tag_name('a')
            names.append(link.text)

        return names

    def get_ids_displayed(self):
        # click on id slider...
        # wait for javascript table to load

        table_elements = self.driver.get_elements_by_xpath('/html/body/div[6]/div/div[3]/div[2]/div/div/div[2]/section/div/div[3]/div[3]/div[2]/table/tbody/tr')
        
        ids = []
        for table_element in table_elements:
            player_id = table_element.find_element_by_class_name('player-id')
            ids.append(player_id.text)

        return ids

    def get_scores_displayed(self):
        data_rows = self.driver.get_elements_by_xpath('//*[@id="stats_grid"]/tbody/tr')
        scores = []

        for row in data_rows:
            cols = row.find_elements_by_tag_name('td')
            
            score_span = cols[len(cols)-1].find_element_by_tag_name('span')
            scores.append(score_span.text)
        
        return scores


    def set_players_displayed(self, number):
        wrapper = self.driver.get_element_by_class('show-player-id')
        link = wrapper.find_element_by_link_text(str(number))
        link.click()
