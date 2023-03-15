import pandas as pd
import numpy as np

data = pd.read_csv('baza.csv')
df = pd.DataFrame(data)

array = np.array(df)
arrayDiabetes = [row[0] for row in array]


countDiabetes = len(arrayDiabetes)

def percent_value(date,sum):
    return round(date / sum * 100, 2)
