class Page:
    
    def __init__(self, driver, url, navigate=False):
        self.driver = driver
        self.url = url

        if navigate:
            self.driver.navigate(url)
    
    def get_title(self):
        return self.driver.get_title()
    
    def navigate(self, url):
        self.driver.navigate(url)

    def click_element(self, element):
        element.click()

    def get_element_text(self, element):
        return element.get_attribute("value")