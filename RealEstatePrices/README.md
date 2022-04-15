
Displaying real estate prices with Flask.

This program requires the user to input the url or path to the csv file that will be parsed. I saved a csv locally for this (path was pasted in code as a comment, flaskapp.py line 29). 

It then targets sale prices and uses other data in the set to predict housing prices. It splits training and validation data to fit the models that are going to be used to take the mean absolute error in three different methods: Decision tree, Decision tree with a maximum limit of 100 and Random Forest. The database stores the MAE results between these three for the user to query later. 
