import requests 
from bs4 import BeautifulSoup 
  
URL = "https://www.x-rates.com/table/?from=USD&amount=1"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser') 
ratelist = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")

for tableVal in ratelist:
	trList = tableVal.findAll('tr')
	for trVal in trList[:6]:
		print(trVal.text)
