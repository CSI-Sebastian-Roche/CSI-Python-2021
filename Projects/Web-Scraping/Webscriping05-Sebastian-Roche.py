import bs4 
import requests
import bs4

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.2037&lon=-67.1469#.Yks1ApPMK3J")
forcast = bs4.BeautifulSoup(website.content, "html.parser")
sevenDay = forcast.find(id="seven-day-forecast")
forcast_items = sevenDay.find_all(class_="tombstone-container")
tonight = forcast_items[1]
#print(tonight.prettify())
cope = tonight.find(class_="period-name").get_text()
print(cope)
period = tonight.find(class_="short-desc").get_text()
print(period)
description = tonight.find(class_="temp temp-low").get_text()
print(description)