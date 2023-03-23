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

print(X_train.describe().T)
print(X_test.describe().T)

plt.figure(figsize=(20,15))
p=sns.heatmap(X_train.corr(),annot=True,cmap='Reds')
plt.show()
