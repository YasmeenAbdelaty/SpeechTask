from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class infow():
    def __init__(self):
        #self.drive = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        s = Service('Chromedriver PATH')
        self.drive=webdriver.Chrome(service=s)
    def get_info(self, query):
        self.query=query
        self.drive.get(url="https://www.wikipedia.org/")
        search = self.drive.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.drive.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        enter.click()



