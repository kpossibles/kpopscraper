import requests
import csv
from bs4 import BeautifulSoup
import json
import sys
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Script takes about 45 minutes to complete

def clearline(msg):
    CURSOR_UP_ONE = '\033[K'
    ERASE_LINE = '\x1b[2K'
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE+'\r')
    print(msg, end='\r')

url = "https://kpopping.com/profiles/the-groups"
page = requests.get(url)

#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(page.content,'html.parser')

#get the HTML of the table called site Table where all the links are displayed
main_table = soup.find("div", attrs={'class': 'widget shadowed pink-bordered'})
idols = main_table.find_all('a', href=True)

#from each link extract the text of link and the link itself
#List to store a dict of the data we extracted
idol_links = []
for link in idols:
    url = "https://kpopping.com" + link['href']
    idol_links.append(url)

print("Starting kpop-artist-links.py - Links grabbed!")
print("Length of list:", len(idol_links))

# Create a file to write to, add headers row
f = csv.writer(open('z-group-names.csv', 'w', encoding="utf-8"))
f.writerow(['name', 'kor_name', 'members', 'facebook', 'twitter', 'vlive', 'instagram', 'youtube', 'website', 'profilepic', 'url', 'bio', 'id'])

idol_data = []

def find_social(str):
    if soup1.find("a", attrs={'class': str}) != None:
        return soup1.find("a", attrs={'class': str})['href']
    else:
        return ""

for index, url in enumerate(idol_links):
    clearline("{} URL {}".format(index, url))
    page1 = requests.get(url)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    data = soup1.find(
        "div", attrs={'class': 'profile-group'})
    name = data.find('h1').text.strip()
    kor_name=''
    if data.find('p', attrs={'class': 'aka'}) !=None:
        kor_name = data.find('p', attrs={'class': 'aka'}).text.strip()
    members = data.find_all("div", attrs={'class': 'member'})
    member_list = []
    for member in members:
        member_list.append(""+member.find("a").text.strip())

    profilepic = "https://kpopping.com" + soup1.find(
        "div", attrs={'class': 'col encyclopedia-sidebar-picture'}).find('img')['src']
    
    facebook=find_social('fab fa-facebook act')
    twitter=find_social('fab fa-twitter act')
    vlive=find_social('fab fa-angellist act')
    instagram=find_social('fab fa-instagram act')
    youtube=find_social('fab fa-youtube act')
    website=find_social('fab fa-chrome act')

    biodiv = soup1.find(
        "div", attrs={'class': 'col box box-encyclopedia shadowed pink-bordered'})
    biotext = ""
    if biodiv.find('p'):
        bio = biodiv.find_all('p')
        bio1 = bio[0].text.strip()
        if len(bio) > 1:
            bio2 = bio[1].text.strip()
            biotext = bio1+". "+bio2
        else:
            biotext=bio1+"."
    record = {
        'name': name,
        'kor_name': kor_name,
        'members': member_list,
        'facebook':facebook,
        'twitter':twitter,
        'vlive':vlive,
        'instagram': instagram,
        'youtube':youtube,
        'website':website,
        'profilepic': profilepic,
        'url': url,
        'bio': biotext,
        'id': index
    }
    # print(record)

    idol_data.append(record)
    
    f.writerow([name, kor_name, member_list, facebook, twitter, vlive, instagram, youtube, website, profilepic,url,biotext,index])
    # clearline('SAVED '+name)

with open('kpop-groups.json', 'w', encoding="utf-8") as outfile:
    json.dump(idol_data, outfile)
#print(idol_data)
