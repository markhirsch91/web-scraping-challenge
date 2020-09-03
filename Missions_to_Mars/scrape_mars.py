from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


# Converting Jupyter Notebook to a Python Script

def init_browser():
    executable_path = {"executable_path":"C:\WebDriver/chromedriver"}
    return Browser("chrome",**executable_path,headless=Flase)


# The data being scraped below will be stored in this mars_data dictionary
mars_data = {}

def nasa_mars_news():
     browser = init_browser()
     news_url = 'https://mars.nasa.gov/news/'
     browser.visit(news_url)
     html = browser.html
     soup = BeautifulSoup(html, 'html.parser')
     news_title = soup.find("li", class_="slide").find('div', class_='content_title').text
     news_p = soup.find("div", class_="article_teaser_body").text
     mars_data['news_title'] = news_title
     mars_data['news_p'] = news_p
     return mars_data