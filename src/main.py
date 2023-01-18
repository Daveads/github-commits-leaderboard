import requests
from bs4 import BeautifulSoup
import re


with open("challenger.txt", 'r') as f:
    text = f.read()

NAMES = text.split()

for i in NAMES:
    URL = ("https://github.com/%s?tab=overview&from=2023-01-01&to=2023-01-16" % i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("h2", {"class": "f4 text-normal mb-2"}).text.strip().replace("\n","")

    strfmt = re.sub("\s+", " ", results)

    print(i, strfmt)
    print(strfmt.split())


