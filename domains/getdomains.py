# -*- coding: utf8 -*-  
import requests

lastNamesFile = open("lastnames.txt", "r")
lastnames = lastNamesFile.read().split("\n")
lastNamesFile.close()

availableDomains = open("availabledomains.txt", "a+")

test = lastnames[:5]
print(test)

for name in test:
    response = requests.post("https://registry.domain.fi/search/fi/app/DomainSearch", data={"DomainName":name})
    print(response.status_code, response.reason)
    print(response.text)
    if '"Available":true' in response.text:
        print(name+" available")
        availableDomains.write(name+"\n")
    else:
        print(name+" not available")
availableDomains.close()
