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

url = "https://kpopping.com/profiles/the-idols"
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

# Create a file to write to, add headers row
f = csv.writer(open('z-artist-names.csv', 'w', encoding="utf-8"))
f.writerow(['Stage Name', 'Real Name', 'Group', 'Instagram', 'Profile Pic', 'Kpopping Profile', 'Bio', 'ID'])

idol_data = []
print("Length of list:", len(idol_links))
for index, url in enumerate(idol_links):
    page1 = requests.get(url)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    main_table1 = soup1.find(
        "div", attrs={'class': 'col encyclopedia-sidebar-picture'})
    data = soup1.find(
        "div", attrs={'class': 'data'})
    stage_name = data.find('h1').text.strip()
    name = data.find('h2').text.strip()
    group = data.find("td", text="Group(s)")
    if group != None:
        group = group.find_next_sibling("td").text
    else:
        group = ""
    profilepic = "https://kpopping.com" + main_table1.find('img')['src']
    instagram = soup1.find(
        "a", attrs={'class': 'fab fa-instagram act'})
    if instagram != None: 
        instagram = instagram['href']
    else:
        instagram = ""
    biodiv = soup1.find(
        "div", attrs={'class': 'profile-group'})
    bio = ""
    if biodiv.find('p'):
        bio = biodiv.find('p').text.strip()
    record = {
        'stage_name': stage_name,
        'real_name': name,
        'group': group,
        'instagram': instagram,
        'profilepic': profilepic,
        'url': url,
        'bio': bio,
        'id': index
    }
    idol_data.append(record)
    f.writerow([stage_name, name, group, instagram, profilepic,url,bio,index])
    clearline('SAVED '+stage_name)


profiles = {
    'profiles': idol_data
}
with open('kpop-profiles.json', 'w') as outfile:
    jsondata = json.dumps(profilesoutfile, sort_keys=True)
#print(idol_data)
