from bs4 import BeautifulSoup
import requests
import json
class Scraper:
    def __init__(self,site):
        self.site = site


    def connect(self):
        self.r = requests.get(self.site)
        self.soup = BeautifulSoup(self.r.text,"lxml")


    def parse(self):
        self.allnews = self.soup.findAll("a",class_="DY5T1d RZIKme")
        for self.news in self.allnews:
            self.newstext = self.news.text
            self.newshref = "https://news.google.com/" + self.news.get("href")
            print(f"{self.newstext}==>{self.newshref}")















pizza = Scraper("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtUmxHZ0pEU0NnQVAB?hl=ru&gl=RU&ceid=RU:ru")
pizza.connect()
pizza.parse()





