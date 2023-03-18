import pandas as pd
import numpy as np

data = pd.read_csv('baza.csv')
df = pd.DataFrame(data)

array = np.array(df)
arrayDiabetes = [row[0] for row in array]
arrayHP = [row[1] for row in array]
arrayChol = [row[2] for row in array]
arrayCholCheck = [row[3] for row in array]
arraySmoker = [row[5] for row in array]
arrayStroke = [row[6] for row in array]
arrayHDA = [row[7] for row in array]
arrayActivity = [row[8] for row in array]
arrayFruits = [row[9] for row in array]
arrayVeggies = [row[10] for row in array]
arrayAlcohol = [row[11] for row in array]
arrayHealthCare = [row[12] for row in array]
arrayNoDocbcCost = [row[13] for row in array]
arrayDiffWalk = [row[17] for row in array]
arraySex = [row[18] for row in array]


countDiabetes = len(arrayDiabetes)


def percent_value(date, sum):
    return round(date / sum * 100, 2)


def compareDateAndDiabetesValue(i, zero_zero, one_zero, two_zero):
    if arrayDiabetes[i] == 0.0: zero_zero = zero_zero + 1
    if arrayDiabetes[i] == 1.0: one_zero = one_zero + 1
    if arrayDiabetes[i] == 2.0: two_zero = two_zero + 1


def fillArrayAllDate(array, percentValueAllDate, countDiabetes):
    for i in range(len(array)):
        percentValueAllDate.append(percent_value(array[i], countDiabetes))


def fillArrayTypeDate(array, percentValue, countTypeDiabetes, countTypePrediabetes, countTypeNodiabetes):
    percentValue.append(percent_value(array[0], countTypeDiabetes))
    percentValue.append(percent_value(array[1], countTypeDiabetes))
    percentValue.append(percent_value(array[2], countTypePrediabetes))
    percentValue.append(percent_value(array[3], countTypePrediabetes))
    percentValue.append(percent_value(array[4], countTypeNodiabetes))
    percentValue.append(percent_value(array[5], countTypeNodiabetes))
