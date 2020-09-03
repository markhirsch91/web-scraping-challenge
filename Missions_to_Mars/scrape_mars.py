from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pymongo


# Converting Jupyter Notebook to a Python Script

def init_browser():
    executable_path = {"executable_path":"C:\WebDriver/chromedriver"}
    return Browser("chrome",**executable_path,headless=Flase)


# The data being scraped below will be stored in this mars_data dictionary
mars_data = {}

# NASA Mars News

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

def mars_space_image():
     browser = init_browser()
     nasa_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
     browser.visit(nasa_image_url)
     featured_img_html = browser.html
     soup = BeautifulSoup(featured_img_html, 'html.parser')

     featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('article')['style'].replace('background-image: url(','').replace(');','').replace("'","")
     mars_data['featured_image_url'] = featured_image_url
     return mars_data

def mars_facts():
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)
    mars_facts_html = browser.html
    soup = BeautifulSoup(mars_facts_html, 'html.parser')

    tables = pd.read_html(mars_facts_url)
    mars_fact_table_df = tables[0]
    mars_fact_table_df.columns = ['Label','Value']
    mars_fact_table_df.set_index('Label',inplace=True)
    facts_html_table = mars_fact_table_df.to_html()
    mars_data['mars_facts'] = mars_facts
    return mars_data

def mars_hemispheres():
    mars_hems_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hems_url)
    mars_hems_html = browser.html
    soup = BeautifulSoup(mars_hems_html, 'html.parser')

    sections = soup.find_all("div", class_="item")

    base_url_hems = 'https://astrogeology.usgs.gov'
    image_urls_hems = []
    for section in sections:
        title_return = section.find('h3').text
        initial_img_link_return = section.find('a', class_='itemLink product-item')['href']
        browser.visit(base_url_hems + initial_img_link_return)
        initial_img_link_return = browser.html
        soup = BeautifulSoup(initial_img_link_return,'html.parser')
        img_url = base_url_hems + soup.find('img', class_='wide-image')['src']
        image_urls_hems.append({"title": title_return, "img_url": img_url})
    mars_data['image_urls_hems'] = image_urls_hems

    return mars_data