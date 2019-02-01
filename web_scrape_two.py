from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all("article")
with open("blog_data.csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['title', 'link', 'date'])

    for a in articles:
        a_tag = a.find('a')
        title = a_tag.get_text()
        url = a_tag['href']
        date = a.find('time')['datetime']
        csv_writer.writerow([title, url, date])



