import requests
from lxml import html
import os

response = requests.get("http://www.tuomas.salste.net/suku/nimi/index-lista.html")
#soup = BeautifulSoup(response.text, "html.parser")
#tags = soup.findAll("a")[6:]

lastNames = open("lastnames.txt","w+")
doc = html.fromstring(response.content)
a_elements = doc.xpath("//a")[6:]

for name in a_elements[:-5]:
    print(name.text_content())
    lastNames.write(name.text_content()+"\n")
lastNames.close()

os.system("sort -o lastnames.txt lastnames.txt")


