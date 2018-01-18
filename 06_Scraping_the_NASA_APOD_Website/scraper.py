# Script that will allow us to download all the NASA APOD images
import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "./img"

if not os.path.exists(download_directory):
    os.makedirs(download_directory)

content = urllib.request.urlopen(base_url).read()

for link in BeautifulSoup(content, "lxml").findAll("a"):
    
    print("Following link: ", link)

    href = urljoin(base_url, link["href"])
    content = urllib.request.urlopen(href).read()

    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(base_url, img["src"])
    
        print("Downloading image: ", img_href)
        
        img_name = img_href.split("/")[-1]
        try: 
            urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
        except urllib.error.HTTPError as e:
            print(e.reason)

