import sqlite3

if __name__ == "__main__":

	con = sqlite3.connect('closedprices.db')
	cur = con.cursor()
	
	"""
	All of these work

	"""
	cur.execute("SELECT Dates FROM prices")
	rows = cur.fetchall()
	print(rows)

	cur.execute("SELECT closedprices FROM prices")
	rows2 = cur.fetchall()
	print(rows2)

	cur.execute("SELECT Dates, closedprices FROM prices Where closedprices = '128.96' ")
	rows3 = cur.fetchall()
	print(rows3)

	cur.execute("SELECT Dates FROM prices Where Dates = 'Dec 11, 2020' ")
	rows4 = cur.fetchall()
	print(rows4)
