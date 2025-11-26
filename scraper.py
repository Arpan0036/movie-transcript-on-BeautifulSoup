from bs4 import BeautifulSoup
import requests

url='https://subslikescript.com/'
url2='https://subslikescript.com'

request=requests.get(url)
content=request.text
soup=BeautifulSoup(content,'lxml')

box=soup.find('ul', class_="scripts-list")
list=box.find_all('a', href=True)

links=[]
for link in list:
    links.append(link['href'])

for link in links:
    movieweb = f'{url2}{link}'
    request2 = requests.get(movieweb)
    content2 = request2.text
    soup2 = BeautifulSoup(content2, 'lxml')

    box2 = soup2.find('article', class_="main-article")
    title = box2.find('h1').get_text()
    transcript = box2.find('div', class_="full-script").get_text(strip=True, separator=" ")

    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)
