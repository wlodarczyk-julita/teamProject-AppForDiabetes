# Import libraries
import  scipy
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
from skfeature.function.similarity_based import fisher_score

base = pd.read_csv('baza.csv')
X = base[['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
          'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
          'GenHlth', 'MentHlth', 'PhysHlth','DiffWalk','Sex','Age','Education','Income']]
Y = base[['Diabetes_012']]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 100)

ranks = fisher_score.fisher_score(X,Y)

feat_importances = pd.Series(ranks, index =['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
          'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
          'GenHlth', 'MentHlth', 'PhysHlth','DiffWalk','Sex','Age','Education','Income'])
feat_importances.plot(kind='barh', color='teal')
plt.show()