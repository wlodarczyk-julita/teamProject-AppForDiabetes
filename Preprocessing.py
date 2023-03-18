import Diabetes
import LoadDate
import pandas as pd
def save (array, arrayAllDate, arrayTypicalDate, name, name1, name2):
    rawDate = { name: array,
               name1: arrayAllDate,
               name2: arrayTypicalDate,
    }
    df = pd.DataFrame(rawDate, columns=[name, name1, name2])
    df.to_csv(name+'.csv', index=False, header=True)


def preprocess (zero_zero, one_zero, two_zero, zero_one, one_one, two_one, arrayElement, name ):
    for i in range(LoadDate.countDiabetes):
        if arrayElement[i] == 0.0:
            if LoadDate.arrayDiabetes[i] == 0.0: zero_zero = zero_zero + 1
            if LoadDate.arrayDiabetes[i] == 1.0: one_zero = one_zero + 1
            if LoadDate.arrayDiabetes[i] == 2.0: two_zero = two_zero + 1
        if arrayElement[i] == 1.0:
            if LoadDate.arrayDiabetes[i] == 0.0: zero_one = zero_one + 1
            if LoadDate.arrayDiabetes[i] == 1.0: one_one = one_one + 1
            if LoadDate.arrayDiabetes[i] == 2.0: two_one = two_one + 1

    information = [zero_zero, zero_one, one_zero, one_one, two_zero, two_one]
    percentValueAllDate = []
    percentValue = []

    LoadDate.fillArrayAllDate(information, percentValueAllDate, LoadDate.countDiabetes)
    LoadDate.fillArrayTypeDate(information, percentValue, Diabetes.no_diabetes, Diabetes.prediabetes,
                               Diabetes.diabetes)
    save(information, percentValueAllDate, percentValue, name, 'Percent analyzing all date:',
                    'Percent analyzing particular date:')


preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayHP, 'HP')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayChol, 'HChol')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayCholCheck, 'HCholCheck')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arraySmoker, 'Smoker')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayStroke, 'Stroke')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayHDA, 'HDA')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayActivity, 'Activity')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayFruits, 'Fruits')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayVeggies, 'Veggies')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayAlcohol, 'Alcohol')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayHealthCare, 'HealthCare')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayNoDocbcCost, 'NoDocbcCost')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arrayDiffWalk, 'Walk')
preprocess(0, 0, 0, 0, 0, 0, LoadDate.arraySex, 'Sex')
