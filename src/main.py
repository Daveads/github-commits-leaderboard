import requests
from bs4 import BeautifulSoup
import re


with open("challenger.txt", 'r') as f:
    text = f.read()

githubUsername = text.split()

data = []


for i in githubUsername:
    URL = ("https://github.com/%s?tab=overview&from=2023-01-01&to=2023-01-16" % i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("h2", {"class": "f4 text-normal mb-2"}).text.strip().replace("\n","")
    
    fullName = soup.find("title").text
    namelgth = len(fullName) - 8

    strfmt = re.sub("\s+", " ", results)

    c = strfmt.split()

    userBoard  = f"{fullName[:namelgth]} {c[0]}"
    
    data.append(userBoard)


#print(data)

def get_commit_per_user(data):
    commit_list = []
    for i in data:
        length = len(i.split()) - 1 
        commit_list.append(int(i.split()[length]))

    return commit_list




def leaderboard_sort(commits, data):
    for i in range(len(commits)):
        for j in range(len(commits) - 1):
            if commits[j] < commits[j + 1]:
                commits[j], commits[j + 1] = commits[j + 1], commits[j]
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


commits = get_commit_per_user(data)

Lead_data = leaderboard_sort(commits, data)


print(" Username >> Name >> commits ")
for i in Lead_data:
    print(i)
