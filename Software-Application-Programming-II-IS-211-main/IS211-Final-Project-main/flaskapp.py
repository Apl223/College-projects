from flask import Flask, render_template, request, redirect
import re,sqlite3
import housingpricestodb
import pandas as pd

query = []
featuresandcsv = []

app = Flask(__name__)

@app.route('/')
def index():
    #had to create a 'template' folder in the same directory as this script for it to find index.html as the template.
    return render_template('index.html', query=query)

@app.route('/submit', methods=['POST'])
def submit():
    con = sqlite3.connect('housingprices.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM MAE")
    rows = cur.fetchall()
    query.append((rows))
    return render_template('index.html', query=query)

@app.route('/submit2', methods=['POST'])
def submit2():
    #link to copy/paste
    #C:\Users\rain\\Desktop\IS211-Course-Project\train.csv
    features = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']
    link = request.form['CSV file']
    home_data = pd.read_csv(link)
    # Create target object and call it y
    y = home_data.SalePrice
    # Create X
    X = home_data[features]
    housingpricestodb.MAE(X,y)
    return render_template('index.html', link=link)

@app.route('/clear', methods=['POST'])
def clear():
    del query[:]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
