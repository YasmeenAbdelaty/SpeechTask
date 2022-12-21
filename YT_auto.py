from selenium import webdriver
from selenium.webdriver.chrome.service import Service
class music():
    def __init__(self):
        #self.drive = webdriver.Chrome(executable_path=r'C:\Users\hp\AppData\Local\Google\Chrome\Application')
        s = Service('Youtube PATH')
        self.drive = webdriver.Chrome(service=s)
    def play(self, query):
        self.query=query
        self.drive.get(url="https://www.youtube.com/results?search_query=" + query)
        #video = self.drive.find_element("xpath",'//*[@id="contents"]/ytd-item-section-renderer')
        #video.click()

