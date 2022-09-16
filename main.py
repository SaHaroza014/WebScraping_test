import requests
from bs4 import BeautifulSoup

url = "http://www.radiostudent.hr/slusas/"
page = requests.get(url)
web_page = page.content  # '.content' instead of '.text' to avoid encoding problems

soup = BeautifulSoup(web_page, "html.parser")
results = soup.find_all(name="td", class_="title column-title")
songs = [song.getText() for song in results]  # list comprehension

with open("songs_recent.txt", mode="w", encoding="utf-8") as file:  # encoding UTF-8
    for value in songs:
        file.write(f'{value}\n')
