#python apple_stocktodb.py
import requests
from bs4 import BeautifulSoup
import sqlite3

if __name__ == "__main__":

	url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

	page = requests.get(url)
	data = page.text
	soup = BeautifulSoup(data,features="html.parser")

	trs = soup.find_all('tr', {'class':'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})
	prices = []
	dates = []
	dateprice = {}
	for tr in trs:

		tds = tr.find_all('td')

		dates.append(tds[0].get_text())
		prices.append(tds[1].get_text())

	#combine 2 arrays into a list of tuples
	dateprice = [(dates[i], prices[i]) for i in range(0, len(dates))]
	for x in dateprice:
		print(x)
	con = sqlite3.connect('closedprices.db')

	with con:
		cur = con.cursor()
		cur.executescript("DROP TABLE IF EXISTS prices")
		cur.execute("CREATE TABLE prices(Dates TEXT, closedprices TEXT)")
		cur.executemany("INSERT INTO prices VALUES(?, ?)", dateprice)	