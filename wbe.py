import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

url = "https://pubmed.ncbi.nlm.nih.gov/"
 
driver = webdriver.Firefox()
driver.get(url)