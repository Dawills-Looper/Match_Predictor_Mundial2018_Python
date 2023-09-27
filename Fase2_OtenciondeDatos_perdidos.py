from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from time import sleep
import pandas as pd

path = "C:/Users/PC SECURITY/Desktop/Fundamentos Proyecto/chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


def get_misssing_data(year):
    web = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"

    driver.get(web)
    matches = driver.find_elements(by='xpath', value='//td[@align="right"]/.. | //td[@style="text-align:right;"]/..')
    # matches = driver.find_elements(by='xpath', value='//tr[@style="font-size:90%"]')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find_element(by='xpath', value='./td[1]').text)
        score.append(match.find_element(by='xpath', value='./td[2]').text)
        away.append(match.find_element(by='xpath', value='./td[3]').text)

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    time.sleep(2)
    return df_football


years = [2002, 2006, 2014, 2022]

fifa = [get_misssing_data(year) for year in years]
driver.quit()
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv("fifa_worldcup_missing_data.csv", index=False)
