# Declare Dependencies 

from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape():

#NASA Mars News
    url1 = 'https://mars.nasa.gov/news/'
    response = requests.get(url1)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('div', class_="content_title")[0].text
    news_p = soup.find_all('div', class_='rollover_description')[0].text
    
    #JPL Mars Space Images - Featured Image
    url2  = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    full_url = soup.find("article", class_="carousel_item")
    full_url = full_url['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    featured_image_url = "https://www.jpl.nasa.gov" + full_url
    
    #Mars Weather
    url3 = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url3)
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    
    #Mars Facts
    url4 = "https://space-facts.com/mars/"
    mars_tabl = pd.read_html(url4)[-1]
    mars_tabl.columns=["Mars Profile ","Values"]
    html_mars_facts = mars_tabl.to_html()
   
    #Mars Hemispheres
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url5)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 1. Cerberus Hemisphere
    mars_1_name='Cerberus Hemisphere'
    mars_1='https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    response = requests.get(mars_1)
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_1_img = soup.find("img", class_="wide-image")
    mars_1_img = mars_1_img['src']
    mars_1_img_url = "https://astrogeology.usgs.gov" + mars_1_img
    
    # 2. Schiaperelli Hemisphere
    mars_2_name='Schiaperelli Hemisphere'
    mars_2='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    response = requests.get(mars_2)
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_2_img = soup.find("img", class_="wide-image")
    mars_2_img = mars_2_img['src']
    mars_2_img_url = "https://astrogeology.usgs.gov" + mars_2_img
    
    # 3.Syrtis Major Hemisphere
    mars_3_name='Syrtis Major Hemisphere'
    mars_3='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    response = requests.get(mars_3)
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_3_img = soup.find("img", class_="wide-image")
    mars_3_img = mars_3_img['src']
    mars_3_img_url = "https://astrogeology.usgs.gov" + mars_3_img
    
    # 4.Valles Marineris Hemisphere
    mars_4_name='Valles Marineris Hemisphere'
    mars_4='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    response = requests.get(mars_4)
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_4_img = soup.find("img", class_="wide-image")
    mars_4_img = mars_4_img['src']
    mars_4_img_url = "https://astrogeology.usgs.gov" + mars_4_img
    
# Create Mars Dictionary
    mars= {'latestmarsnews': news,
           'newspar':  news_p,
           'image': featured_image_url,
           'weather': mars_weather,
           'marsfacts': html_mars_facts,
           'titles1':mars_1_name,"imge_url1":mars_1_img_url,
           'titles2':mars_2_name,"imge_url2":mars_2_img_url,
           'titles3':mars_3_name,"imge_url3":mars_3_img_url,
           'titles4':mars_4_name,"imge_url4":mars_4_img_url 
           }
    return mars     
if __name__ == '__main__':
    scrape()