import os, sys, threading, subprocess, requests, urllib 
from bs4 import BeautifulSoup

# Create  directory 
os.makedirs("Facets365Wallpapers",exist_ok=True)
main_url = "http://www.facets.la/wallpapers/"

res = requests.get(main_url)

print(res.text[0:100])

soup = BeautifulSoup(res.text,'html.parser')

links_list = []
for x in soup.find_all('a'):
	url = x.get('href')
	links_list.append(url)

links_list = links_list[12:len(links_list)]

for link in links_list:
	mini_soup = BeautifulSoup(requests.get(link).text,'html.parser')
	
	for i in mini_soup.find_all('img'):
		mini_link = i.get('src')
		if mini_link.startswith("http://www.facets.la/wallpaper/"):
			myImage = requests.get(mini_link)
			wallpaper_name = mini_link.split('/')[4]
			imageFile = open(os.path.join("Facets365Wallpapers", wallpaper_name), 'wb')
			for data in myImage.iter_content(100000):
				imageFile.write(data)
			imageFile.close()
			print("Downloaded... "+wallpaper_name)

