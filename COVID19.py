from bs4 import BeautifulSoup as soup
import requests

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = soup(r.text, "html.parser")
data = s.find_all("div", class_="maincounter-number")
status = s.find_all("div", class_="number-table-main")
active = s.find_all("span", class_="number-table")
per = s.find_all("strong")
country = s.find_all("td")
cou=[]
for a in country:
    cou.append(a.text)
print("LIVE COVID-19 details using Web-Scraping")
print("enter country name(first letter capital): ")
c=input()
if c=="":
    c="World"
b=cou.index(c)
print(cou[b].upper()+" total cases:"+cou[b+1]+"   new cases:"+cou[b+2]+"   total deaths:"+cou[b+3]+"   new deaths:"+cou[b+4]+"   recovered:"+cou[b+5]+"   active cases:"+cou[b+6]+"   serious cases:"+cou[b+7]+"   cases/1Mpop:"+cou[b+8]+"   deaths/1Mpop:"+cou[b+9]+"   tests:"+cou[b+10]+"  tests/1Mpop:"+cou[b+11])

print("\nGlobal data...")
print("Total cases: " + data[0].text.strip())
print("Total deaths: " + data[1].text.strip())
print("Total recovered: " + data[2].text.strip())
print("Active cases: " + status[0].text.strip() + "\t\t--Mild: " + active[0].text.strip() + " (" + per[
    2].text.strip() + "%)\t\t--Critical: " + active[1].text.strip() + " (" + per[3].text.strip() + "%)")
print("Closed cases: " + status[1].text.strip() + "\t\t--Discharged: " + active[2].text.strip() + " (" + per[
    4].text.strip() + "%)\t--Deaths: " + active[3].text.strip() + " (" + per[5].text.strip() + "%)")
print("Visit WHO website for more info on COVID-19 https://www.who.int/emergencies/diseases/novel-coronavirus-2019")
print("Data source: https://www.worldometers.info/coronavirus/")
