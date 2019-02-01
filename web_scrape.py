from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://www.nhl.com/player/alex-ovechkin-8471214")
soup = BeautifulSoup(html, "html.parser")
goals = soup.select(".season-summary__table-sm table tbody tr td")[1]
print("Goals:",goals.text)