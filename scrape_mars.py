from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

 # results are returned as an iterable list
    results = soup.find('div', class_="content_title")
    news_title = results.find('a').text

    paragraph_text = soup.find('div', class_="rollover_description_inner")
    news_p = paragraph_text.text


    mars["news_title"] = news_title
    mars['paragraph_text']=news_p
#Scraping for feaured image.
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(2)   

    browser.click_link_by_partial_text("more info")

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find('img', class_="main_image")
    featured_image_url ="https://www.jpl.nasa.gov" + results["src"]

    mars["featured_image"]= featured_image_url

#Scraping for mars_fact table
    # url = 'http://space-facts.com/mars/'
    # tables = pd.read_html(url)
    
    # df = tables[0]
    # df.columns = ["Fact", "Measurement"]
    # df.head()
    # html_table = df.to_html()
    # html_table
    # html_table.replace('\n', '')
    # df.to_html('table.html')
    
    # mars["mars_facts"] = df.to_html('table.html')

#Scraping mars weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('p', class_="TweetTextSize")

    for result in results:
   
        if "Sol" in result.text:
            print(result.text)
            mars_weather = result.text
            break

    mars["mars_weather"] = mars_weather[:-26]
#mars hemispheres
#     url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(url)

#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
    
#     title = soup.find_all('h3')

#     for titles in title:
#         hemisphere_title = titles.text
#     mars['hemisphere_title']= hemisphere_title

#     url_list = []

#    for title in (title_list):
#     t=title
#     #print(t)
#     browser.click_link_by_partial_text(t)
#     time.sleep(5)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
#     url_image = soup.find("img", class_="wide-image")
#     url_image['src']
#     image_url ="https://astrogeology.usgs.gov" + url_image['src']
#     url_list.append(image_url)
#     #print(f" title:{t} , img_url:  {image_url}")
#     browser.click_link_by_partial_text("Back")
#     time.sleep(5)
#     #print(titles.text)
    

    return mars
