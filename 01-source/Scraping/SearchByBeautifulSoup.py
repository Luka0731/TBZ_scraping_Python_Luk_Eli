
# |------- step 1: setting everything up -------|

from selenium import webdriver # selenium controls the webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup

# set path to chromedriver
CHROMEDRIVER_PATH = r"C:\Users\lukag\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# initialize webdriver with service
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()

# options
options.add_argument("--window-size=1920,1080")  # set window size
options.add_argument("--disable-blink-features=AutomationControlled") # hide, that it is controlled by selenium
driver = webdriver.Chrome(service=service, options=options)

# open google search url
search_url = "https://www.google.com/search?q=lead+generation+tools&oq=lead+generation+tools"
driver.get(search_url)

time.sleep(3) # wait for the page to load

page_html = driver.page_source
print(page_html)



# |------- step 2: parsing the page and saving it in obj -------|

obj={}
l=[]
soup = BeautifulSoup(page_html,'html.parser')

allData = soup.find("div",{"class":"dURPMd"}).find_all("div",{"class":"Ww4FFb"})
print(len(allData))
for i in range(0,len(allData)):
    try:
        obj["title"]=allData[i].find("h3").text
    except:
        obj["title"]=None

    try:
        obj["link"]=allData[i].find("a").get('href')
    except:
        obj["link"]=None

    try:
        obj["description"]=allData[i].find("div",{"class":"VwiC3b"}).text
    except:
        obj["description"]=None

    l.append(obj)
    obj={}

print(l)



# |------- step 3: saving it in csv file -------|

df = pd.DataFrame(l)
df.to_csv('csv-files/google.csv', index=False, encoding='utf-8')
