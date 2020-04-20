import requests
from bs4 import BeautifulSoup
import pandas

page = requests.get("https://weather.com/en-IN/weather/tenday/l/7472a7bbd3a7454aadf596f0ba7dc8b08987b1f7581fae69d8817dffffc487c2")
soup = BeautifulSoup(page.content,"html.parser")
name_of_prediction = soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text
table = soup.find_all("table",{"class":"twc-table"})
l=[]
for items in table:
 for i in range(len(items.find_all("tr"))-1):
  d = {}  
  d["day"]=items.find_all("span",{"class":"date-time"})[i].text
  d["date"]=items.find_all("span",{"class":"day-detail"})[i].text
  d["desc"]=items.find_all("td",{"class":"description"})[i].text 
  d["temp"]=items.find_all("td",{"class":"temp"})[i].text 
  d["precip"]=items.find_all("td",{"class":"precip"})[i].text
  d["wind"]=items.find_all("td",{"class":"wind"})[i].text  
  d["humidity"]=items.find_all("td",{"class":"humidity"})[i].text 
  l.append(d)
df = pandas.DataFrame(l)
df.to_csv("austin_weather_output.csv")
