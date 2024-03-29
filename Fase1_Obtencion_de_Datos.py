from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [2002, 2006, 2014, 2022]

def get_matches(year):
    web = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, "lxml")
    
    matches = soup.find_all("div", class_="footballbox")
    
    home = []
    score = []
    away = []
    
    for match in matches:
        home.append(match.find("th", class_="fhome").get_text())
        score.append(match.find("th", class_="fscore").get_text())
        away.append(match.find("th", class_="faway").get_text())
        
    dict_football = {"home": home, "score": score, "away": away}
    df_football = pd.DataFrame(dict_football)
    df_football["year"] = year
    return df_football  
        
    
#Data_historica
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv("fifa_worldcup_historical_data.csv", index=False)

#fixture
df_fixture = get_matches("2022")
df_fixture.to_csv("fifa_worldcup_fixture.csv", index=False)
