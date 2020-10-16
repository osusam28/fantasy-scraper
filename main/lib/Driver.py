from selenium import webdriver
from selenium.webdriver.common.by import By

import logging


class Driver:

    logger = logging.getLogger(__name__)

    HEADLESS_OPTION = 'headless'

    WINDOW_SIZE_OPTION = 'window-size=1200x600'

    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()

        if headless:
            logging.debug('adding argument [{}]'.format(Driver.HEADLESS_OPTION))
            options.add_argument(Driver.HEADLESS_OPTION)
        
        logging.debug('adding argument [{}]'.format(Driver.WINDOW_SIZE_OPTION))
        options.add_argument(Driver.WINDOW_SIZE_OPTION)

        logging.debug('creating driver ...')
        self.driver = webdriver.Chrome(executable_path='/home/sam/Documents/scraper/chromedriver', chrome_options=options)

    def get_driver(self):
        return self.driver

    def get_title(self):
        return self.driver.title
    
    def navigate(self, url):
        self.driver.get(url)

    def get_element_by_class(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def get_element_by_id(self, id):
        return self.driver.find_element(By.ID, id)

    def get_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def get_elements_by_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def get_element_by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def get_element_by_link_text(self, text):
        return self.driver.find_element_by_link_text(text)
    
    def close(self):
        self.driver.quit()
