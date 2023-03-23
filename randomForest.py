# Import libraries
import  scipy
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


# Upload the dataset
base = pd.read_csv('baza.csv')
# print(base)

# Create features and target
# X = base[['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth','DiffWalk','Sex','Age','Education','Income']]
X = base[['HighBP', 'BMI', 'Smoker', 'PhysActivity', 'Fruits', 'Veggies', 'GenHlth', 'MentHlth', 'PhysHlth', 'Sex','Age']]
Y = base[['Diabetes_012']]
# print(X)
# print(Y)

# Split data into training and test sets
# test_size -  represent the proportion of the dataset to include in the test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 100)

# Train the model
#n_estimators - The number of trees in the forest.
regr = RandomForestRegressor(n_estimators = 300, max_depth = 30, random_state = 30)
#Return a contiguous flattened array.
regr.fit(X_train, y_train.values.ravel())

# Make prediction
#It returns the labels of the data passed as argument based upon the learned or trained data obtained from the model.
predictions = regr.predict(X_test)

result = X_test
result['Diabetes'] = y_test
result['prediction'] = predictions.tolist()
# print(result)


#To estimate our model more precisely, we will look at Mean absolute error (MAE), Mean squared error (MSE), and R-squared scores.
# Mean absolute error (MAE)
mae = mean_absolute_error(y_test.values.ravel(), predictions)

# Mean squared error (MSE)
mse = mean_squared_error(y_test.values.ravel(), predictions)

# R-squared scores
r2 = r2_score(y_test.values.ravel(), predictions)

# Print metrics
print('Mean Absolute Error:', round(mae, 2))
print('Mean Squared Error:', round(mse, 2))
print('R-squared scores:', round(r2, 2))

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV

# Find the best parameters for the model
# parameters = {
#     'max_depth': [10, 20, 30, 40],
#     'n_estimators': [100, 200, 300]
# }
# gridforest = GridSearchCV(regr, parameters, cv = 3, n_jobs = -1, verbose = 1)
# gridforest.fit(X_train, y_train.values.ravel())
# gridforest.best_params_
# print(gridforest.best_params_)

# Get features list
characteristics = X.columns

# Get the variables importances, sort them, and print the result
importances = list(regr.feature_importances_)
characteristics_importances = [(characteristic, round(importance, 2)) for characteristic, importance in zip(characteristics, importances)]
characteristics_importances = sorted(characteristics_importances, key = lambda x: x[1], reverse = True)
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in characteristics_importances];

# Visualize the variables importances
plt.bar(characteristics, importances, orientation = 'vertical')
plt.xticks(rotation = 'vertical')
plt.ylabel('Importance')
plt.xlabel('Variable')
plt.grid(axis = 'y', color = '#D3D3D3', linestyle = 'solid')
plt.show()

# T służy do transpozycji indeksu i kolumn ramki danych.

# DataFrame zawiera dane liczbowe, opis zawiera następujące informacje dla każdej kolumny:
# count — liczba niepustych wartości.
# mean - Średnia (średnia) wartość.
# std — odchylenie standardowe.
# min - wartość minimalna.
# 25% — percentyl 25%*.
# 50% — percentyl 50%*.
# 75% — percentyl 75%*.
# max - maksymalna wartość.
#*Percentyl znaczenie: ile wartości jest mniejszych od podanego percentyla.

# print(train.describe().T)
# print(test.describe().T)

# plt.figure(figsize=(20,15))
# p=sns.heatmap(train.corr(),annot=True,cmap='Reds')
# plt.show()
#
# model = RandomForestClassifier(n_estimators=1000, max_depth=10)
# model.fit(X_train, y_train)