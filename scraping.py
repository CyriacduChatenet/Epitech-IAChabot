from bs4 import BeautifulSoup
import pandas 
import time
import requests
import pandas
 
base_url = 'https://www.bbc.co.uk/sport/football/european-championship/scores-fixtures'
start_date = 2023
end_date = 2024
# the start date and end date
 
tournament_dates = []
 
for year in range (start_date, end_date + 1):
    for month in range (1, 13):
        if (month < 10):
            tournament_dates.append(f"{str(year)}-0{str(month)}")
        else :
            tournament_dates.append(f"{str(year)}-{str(month)}")
 
urls = [f"{base_url}/{dt}" for dt in tournament_dates]
 
def show_result(home, home_goals, away, away_goals) -> str:
  return f"{home} {home_goals} - {away_goals} {away}"
 
d = {'home':[], 'away': [], 'home_goals': [], 'away_goals': []}
 
for url in urls:
  time.sleep(1)
  # send the HTTP request, then sleep.
  response = requests.get(url)
  # pass response data to BeautifulSoup
  soup = BeautifulSoup(response.text, 'html.parser')
 
  # get all fixtures on the page
  fixtures = soup.find_all('article', {'class': 'sp-c-fixture'})
 
  # iterate over fixtures to extract data and append to results list
  for fixture in fixtures:
    home = fixture.select_one('.sp-c-fixture__team--home .sp-c-fixture__team-name-trunc')
    away = fixture.select_one('.sp-c-fixture__team--away .sp-c-fixture__team-name-trunc')
    home_goals = fixture.select_one('.sp-c-fixture__number--home')
    away_goals = fixture.select_one('.sp-c-fixture__number--away')
    if (home and away and home_goals and away_goals) :
        d['home'].append(home.text)
        d['away'].append(away.text)
        d['home_goals'].append(home_goals.text)
        d['away_goals'].append(away_goals.text)
 
df = pandas.DataFrame(data=d)
df.to_csv('data.csv')# imports required for the tutorial
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
import pandas
 
# set the BBC base url, and the start and end dates
base_url = 'https://www.bbc.co.uk/sport/football/european-championship/scores-fixtures'
start_date = 2023
end_date = 2024
 
# use the date_range() function from pandas to generate all the days between
# the start date and end date
 
tournament_dates = []
 
for year in range (start_date, end_date + 1):
    for month in range (1, 13):
        if (month < 10):
            tournament_dates.append(f"{str(year)}-0{str(month)}")
        else :
            tournament_dates.append(f"{str(year)}-{str(month)}")
 
urls = [f"{base_url}/{dt}" for dt in tournament_dates]
 
def show_result(home, home_goals, away, away_goals) -> str:
  return f"{home} {home_goals} - {away_goals} {away}"
 
d = {'home':[], 'away': [], 'home_goals': [], 'away_goals': []}
 
for url in urls:
  time.sleep(1)
  # send the HTTP request, then sleep.
  response = requests.get(url)
  # pass response data to BeautifulSoup
  soup = BeautifulSoup(response.text, 'html.parser')
 
  # get all fixtures on the page
  fixtures = soup.find_all('article', {'class': 'sp-c-fixture'})
 
  # iterate over fixtures to extract data and append to results list
  for fixture in fixtures:
    home = fixture.select_one('.sp-c-fixture__team--home .sp-c-fixture__team-name-trunc')
    away = fixture.select_one('.sp-c-fixture__team--away .sp-c-fixture__team-name-trunc')
    home_goals = fixture.select_one('.sp-c-fixture__number--home')
    away_goals = fixture.select_one('.sp-c-fixture__number--away')
    if (home and away and home_goals and away_goals) :
        d['home'].append(home.text)
        d['away'].append(away.text)
        d['home_goals'].append(home_goals.text)
        d['away_goals'].append(away_goals.text)
df = pandas.DataFrame(data=d)
df.to_csv('data.csv')