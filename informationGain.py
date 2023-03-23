# Import libraries
import  scipy
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

base = pd.read_csv('baza.csv')
X = base[['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
          'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
          'GenHlth', 'MentHlth', 'PhysHlth','DiffWalk','Sex','Age','Education','Income']]
Y = base[['Diabetes_012']]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 100)

importances = mutual_info_classif(X, Y)
feat_importances = pd.Series(importances, index =['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
          'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
          'GenHlth', 'MentHlth', 'PhysHlth','DiffWalk','Sex','Age','Education','Income'])
feat_importances.plot(kind='barh', color='teal')
plt.show()

characteristics = X.columns

# Get the variables importances, sort them, and print the result
importances = list(importances)
characteristics_importances = [(characteristic, round(importance, 2)) for characteristic, importance in zip(characteristics, importances)]
characteristics_importances = sorted(characteristics_importances, key = lambda x: x[1], reverse = True)
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in characteristics_importances];