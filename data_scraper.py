from bs4 import BeautifulSoup
import requests
import json

#Setup
URL = "https://www.sunnyportal.com/Templates/PublicPage.aspx?page=6d806835-63f7-4577-ab4c-8116de0ec142"

def scrapeData(url):
    response = requests.get(url)
    return BeautifulSoup(response.content,"html.parser")

def getData(html):
    titles = ("currentPower", "energy", "co2Avoided")
    page = html.find_all("span", class_="mainValueAmount")
    values = [None for x in range(3)]
    for x in range(3):
        values[x] = page[x].get_text()
    return dict(zip(titles,values))


def writeOut(data):
    with open("data.json", "w") as writeJSON:
        json.dump(data,writeJSON)


page = scrapeData(URL)
data = getData(page)
writeOut(data)
