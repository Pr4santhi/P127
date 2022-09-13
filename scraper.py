#Selenium opens a web page in the browser
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
#The url for the Nasa website
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
#Web driver will help us open chrom browser with selenium
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
#Getting the data from the URL
browser.get(START_URL)
#Makes our code sleep until the web page is loaded properly
time.sleep(10)

def scrape():
#Storing the headers from the website
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink"]
    planet_data = []
    for i in range(1, 5):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        #Check page number 
        current_page_num=int()
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
                        #creating a variable callbed hyperlink_li_tag 
            hyperlink_li_tag=li_tags[0]
            #To find all the a tags with href
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a",href=True)[0]["href"])
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
