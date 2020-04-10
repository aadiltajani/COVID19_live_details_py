from bs4 import BeautifulSoup as soup
import requests
url ="https://www.worldometers.info/coronavirus/"
r=requests.get(url)
s=soup(r.text,"html.parser")
data=s.find_all("div",class_="maincounter-number")
status=s.find_all("div",class_="number-table-main")
active=s.find_all("span",class_="number-table")
per=s.find_all("strong")
#mild=active[0].text.strip()
#act=status[0].text.strip()
print("LIVE COVID-19 details")
print("Total cases: "+data[0].text.strip())
print("Total deaths: "+data[1].text.strip())
print("Total recovered: "+data[2].text.strip())
print(len(per),per[0].text.strip())
print("Active cases: "+status[0].text.strip()+"\t\t--Mild: "+active[0].text.strip()+" ("+per[0].text.strip()+"%)\t\t--Critical: "+active[1].text.strip()+" ("+per[1].text.strip()+"%)")
print("Closed cases: "+status[1].text.strip()+"\t\t--Discharged: "+active[2].text.strip()+" ("+per[2].text.strip()+"%)\t--Deaths: "+active[3].text.strip()+" ("+per[3].text.strip()+"%)")
print("Visit WHO website for more info on COVID-19 https://www.who.int/emergencies/diseases/novel-coronavirus-2019")

