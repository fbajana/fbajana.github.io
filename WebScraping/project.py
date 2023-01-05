import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

serv = Service('C:/Users/0Zero/OneDrive/Desktop/Python CIS 403/Week 18/project/chromedriver_win32/chromedriver.exe')

driver = webdriver.Chrome(service=serv)
driver.get('https://robertsspaceindustries.com/store/pledge/browse/game-packages/?sort=weight&direction=desc')
results = []
other_results = []
time.sleep(2)
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.findAll(attrs='ItemWidget-main'):
    head = a.find('h3')
    if head not in results:
        results.append(head.text)

i = 1
for b in soup.findAll(attrs='Price-price'):
    name = b.find('span')
    if name not in other_results:
        if i < 13 and i % 2 == 0:
            other_results.append(name.text)
        elif i >= 13:
            other_results.append(name.text)
        i += 1

driver.close()
df = pd.DataFrame({'Name': results, 'Price': other_results})
df.to_csv('name.csv', index=False, encoding='utf-8')