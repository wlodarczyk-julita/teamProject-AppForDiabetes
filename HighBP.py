import Diabetes
import LoadDate
import SaveToFIle

arrayHP = [row[1] for row in LoadDate.array]

zero_zeroHP = 0
one_zeroHP = 0
two_zeroHP = 0

zero_oneHP = 0
one_oneHP = 0
two_oneHP = 0

for i in range(LoadDate.countDiabetes):
    if arrayHP[i] == 0.0:
        if LoadDate.arrayDiabetes[i] == 0.0: zero_zeroHP = zero_zeroHP + 1
        if LoadDate.arrayDiabetes[i] == 1.0: one_zeroHP = one_zeroHP + 1
        if LoadDate.arrayDiabetes[i] == 2.0: two_zeroHP = two_zeroHP + 1
    if arrayHP[i] == 1.0:
        if LoadDate.arrayDiabetes[i] == 0.0: zero_oneHP = zero_oneHP + 1
        if LoadDate.arrayDiabetes[i] == 1.0: one_oneHP = one_oneHP + 1
        if LoadDate.arrayDiabetes[i] == 2.0: two_oneHP = two_oneHP + 1

informationHP = [zero_zeroHP, zero_oneHP, one_zeroHP,one_oneHP, two_zeroHP,two_oneHP]
percentValueAllDateHP = []
percentValueHP = []

LoadDate.fillArrayAllDate(informationHP, percentValueAllDateHP, LoadDate.countDiabetes)
LoadDate.fillArrayTypeDate(informationHP, percentValueHP, Diabetes.no_diabetes, Diabetes.prediabetes, Diabetes.diabetes)
SaveToFIle.save(informationHP, percentValueAllDateHP, percentValueHP, 'HP','Percent analyzing all date:','Percent analyzing particular date:' )
