import urllib.request
from io import StringIO
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
page = urllib.request.urlopen(url).read().decode("ascii","ignore")
d = StringIO(page)
soup = BeautifulSoup(d.read(),features="html.parser")

trs = soup.find_all('tr')

top20Counter = 0

for tr in trs:
    tds = tr.find_all("td")

    try:
        names = str(tds[0].get_text())
        touchdowns = tds[8].get_text()

    except:
        continue
    top20Counter += 1
    if top20Counter > 20:
        break

    print("Name:{}".format(names))
    print("Touchdowns{}".format(touchdowns))
