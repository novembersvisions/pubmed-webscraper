import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

url = "https://pubmed.ncbi.nlm.nih.gov/"

# connect to firefox webdriver 
driver = webdriver.Firefox()
driver.get(url)

# put search term into pubmed
element = driver.find_element_by_xpath ('//*[@id="id_term"]')
element.send_keys('neuromorphic')

# click the box
element = driver.find_element_by_xpath ('/html/body/div[2]/main/div[1]/div/form/div/div[1]/div/button/span')
element.click()

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', {'id' : 'nameSearch'})
article_profiles = all_divs.find_all()

count = 0
for article_profile in article_profiles :
    print(article_profile.text)
    count = count + 1
    if(count == 20) :
        break

driver.close()


