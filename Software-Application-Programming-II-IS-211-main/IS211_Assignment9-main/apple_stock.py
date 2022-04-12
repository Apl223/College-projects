import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data,features="html.parser")

trs = soup.find_all('tr', {'class':'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})

for tr in trs:

	tds = tr.find_all('td')

	try:
		Dates = str(tds[0].get_text())
		closedprices = str(tds[4].get_text())

	except:
		continue

	print("Date:{}".format(Dates))
	print("Closed Prices:{}".format(closedprices))
