import pandas as pd
import numpy as np

import Diabetes

data = pd.read_csv('baza.csv')
df = pd.DataFrame(data)

array = np.array(df)
arrayDiabetes = [row[0] for row in array]


countDiabetes = len(arrayDiabetes)

def percent_value(date,sum):
    return round(date / sum * 100, 2)

def compareDateAndDiabetesValue(i, zero_zero, one_zero, two_zero):
    if arrayDiabetes[i] == 0.0: zero_zero = zero_zero + 1
    if arrayDiabetes[i] == 1.0: one_zero = one_zero + 1
    if arrayDiabetes[i] == 2.0: two_zero = two_zero + 1


def fillArray (array, percentValueAllDate, percentValue, countDiabetes, countTypeDiabetes, countTypePrediabetes, countTypeNodiabetes):
    for i in range(len(array)):
        percentValueAllDate.append(percent_value(array[i], countDiabetes))

        percentValue.append(percent_value(array[0], Diabetes.no_diabetes))
        percentValue.append(percent_value(array[1], Diabetes.no_diabetes))
        percentValue.append(percent_value(array[2], Diabetes.prediabetes))
        percentValue.append(percent_value(array[3], Diabetes.prediabetes))
        percentValue.append(percent_value(array[4], Diabetes.diabetes))
        percentValue.append(percent_value(array[5], Diabetes.diabetes))
