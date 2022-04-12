from flask import Flask, render_template, request, redirect
import re,sqlite3

query = []

app = Flask(__name__)

@app.route('/')
def index():
    #had to create a 'template' folder in the same directory as this script for it to find index.html as the template.
    return render_template('index.html', query=query)


@app.route('/submit', methods=['POST'])
def submit():
    con = sqlite3.connect('closedprices.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM prices")
    rows = cur.fetchall()

    query.append((rows))

    return render_template('index.html', query=query)


@app.route('/clear', methods=['POST'])
def clear():
    del query[:]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)