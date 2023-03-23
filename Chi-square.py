# Import libraries
import  scipy
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import mutual_info_classif, SelectKBest
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.feature_selection import chi2
base = pd.read_csv('baza.csv')
X = base[['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
          'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
          'GenHlth', 'MentHlth', 'PhysHlth','DiffWalk','Sex','Age','Education','Income']]
Y = base[['Diabetes_012']]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 100)

X_cat = X.astype(int)

chi2_features = SelectKBest(chi2, k=12)
X_kbest_features = chi2_features.fit_transform(X_cat, Y)
print(X_kbest_features)
print('Original feature number: ', X_cat.shape[1])
print('Reduced feature number: ', X_kbest_features.shape[1])