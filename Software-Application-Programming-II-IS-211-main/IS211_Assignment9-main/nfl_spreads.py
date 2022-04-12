import urllib.request
from io import StringIO
from bs4 import BeautifulSoup

url = "http://www.footballlocks.com/nfl_point_spreads.shtml"
page = urllib.request.urlopen(url).read().decode("ascii","ignore")
d = StringIO(page)
soup = BeautifulSoup(d.read(),features="html.parser")

trs = soup.find_all('tr')

for tr in trs:

    tds = tr.find_all("td")

    try:
        Favorite = tds[1].get_text()
        Underdog = tds[3].get_text()
    except:
        continue

    print("Favorites: {} | Underdog: {}.".format(Favorite, Underdog))