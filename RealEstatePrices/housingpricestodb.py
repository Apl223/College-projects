#python housingpricestodb.py
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import sqlite3

def MAE(X,y):

	# Split into validation and training data
	train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

	# Specify Model
	iowa_model = DecisionTreeRegressor(random_state=1)
	# Fit Model
	iowa_model.fit(train_X, train_y)

	# Make validation predictions and calculate mean absolute error
	val_predictions = iowa_model.predict(val_X)
	val_mae1 = mean_absolute_error(val_predictions, val_y)
	#print("Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae1))

	# Using best value for max_leaf_nodes
	iowa_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
	iowa_model.fit(train_X, train_y)
	val_predictions = iowa_model.predict(val_X)
	val_mae2 = mean_absolute_error(val_predictions, val_y)
	#print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae2))

	rf_model = RandomForestRegressor()
	# fit your model
	rf_model.fit(train_X, train_y)
	# Calculate the mean absolute error of your Random Forest model on the validation data
	rf_val_predictions = rf_model.predict(val_X)
	rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)
	#print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(rf_val_mae))

	MAE = (val_mae1, val_mae2, rf_val_mae)

	con = sqlite3.connect('housingprices.db')

	with con:
		cur = con.cursor()
		cur.executescript("DROP TABLE IF EXISTS MAE")
		cur.execute("CREATE TABLE MAE(Without_max_leaf INT,With_max_leaf INT, RFM INT)")
		cur.executemany("INSERT INTO MAE VALUES(?,?,?)", (MAE,))


