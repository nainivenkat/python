from bs4 import BeautifulSoup
import requests

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=36.46458&lon=-79.762539").text
soup = BeautifulSoup(page, "lxml")
forecast = soup.find(id = 'seven-day-forecast')

for forecast in forecast.find_all(class_="tombstone-container"):
    day = forecast.p.text
    print day, ":",
    weather = forecast.find(class_="short-desc")
    print weather.text
