# Scraper that download all the images in a website
import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import validators

base_url = input("Enter website's URL. Include http://, etc.: ")
download_directory = "./img"

if validators.domain(base_url):
    print("not a valid url, quitting!")
    quit(0)

if not os.path.exists(download_directory):
    os.makedirs(download_directory)

links_to_visit = set((base_url,))
links_visited = set()

while links_to_visit:
    current_page = links_to_visit.pop()

    print("Visiting page: ", current_page)

    links_visited.add(current_page)
    content = urllib.request.urlopen(current_page).read()

    for link in BeautifulSoup(content, "lxml").findAll("a"):
        absolute_link = urljoin(current_page, link["href"])
        if absolute_link not in links_visited:
            links_to_visit.add(absolute_link)

    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(current_page, img["src"])

        print("...Downloading image: ", img_href)

        img_name = img_href.split("/")[-1]
        
        try:
            urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
        except urllib.error.HTTPError as error:
            print(error.reason)

