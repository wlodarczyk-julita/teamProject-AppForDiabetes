# import numpy as np
# import pandas as pd
# import pickle
# from sklearn import datasets
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# import matplotlib.pyplot as plt
# import pandas as pd
# import csv
#
# import Diabetes
# import LoadDate
#
# import matplotlib.pyplot as plt
#
# import SaveToFIle
#
# arrayFruits = [row[9] for row in LoadDate.array]
#
# # plt.scatter(arrayDiabetes, arrayFruits , label='Klasa 3')
#
# # plt.legend()
# # plt.xlabel('Diabetes')
# # plt.ylabel('Fruits')
# # plt.show()
#
# zero_zeroFruit = 0
# one_zeroFruit = 0
# two_zeroFruit = 0
#
# zero_oneFruit = 0
# one_oneFruit = 0
# two_oneFruit = 0
# for i in range(LoadDate.countDiabetes):
#     if arrayFruits[i] == 0.0:
#         if LoadDate.arrayDiabetes[i] == 0.0: zero_zeroFruit = zero_zeroFruit + 1
#         if LoadDate.arrayDiabetes[i] == 1.0: one_zeroFruit = one_zeroFruit + 1
#         if LoadDate.arrayDiabetes[i] == 2.0: two_zeroFruit = two_zeroFruit + 1
#     if arrayFruits[i] == 1.0:
#         if LoadDate.arrayDiabetes[i] == 0.0: zero_oneFruit = zero_oneFruit + 1
#         if LoadDate.arrayDiabetes[i] == 1.0: one_oneFruit = one_oneFruit + 1
#         if LoadDate.arrayDiabetes[i] == 2.0: two_oneFruit = two_oneFruit + 1
#
#
# informationFruit = [zero_zeroFruit, zero_oneFruit, one_zeroFruit,one_oneFruit, two_zeroFruit,two_oneFruit]
# percentValueAllDateFruit = []
# percentValueFruit = []
#
# LoadDate.fillArrayAllDate(informationFruit, percentValueAllDateFruit, LoadDate.countDiabetes)
# print(informationFruit, percentValueFruit, percentValueAllDateFruit)
# LoadDate.fillArrayTypeDate(informationFruit, percentValueFruit, Diabetes.no_diabetes, Diabetes.prediabetes, Diabetes.diabetes)
# print(informationFruit, percentValueFruit, percentValueAllDateFruit)
# SaveToFIle.save(informationFruit, percentValueAllDateFruit, percentValueFruit, 'Fruit','Percent analyzing all date:','Percent analyzing particular date:' )
#
# # my_data = np.genfromtxt('baza.csv', delimiter=',')
# # np.save('my_dat.npz', my_data)
# # df = pd.read_csv('baza.csv', delimiter=',')
# # df = df.to_numpy()
# # np.save('my_data', df)
#
#
# # with open('baza.csv') as f:
# #   reader = csv.reader(f)
# #  lst = list(reader)
# # #print(lst[0:10])
#
# # array = np.array(lst)
#
# # print(len(array1))
#
# # test = df['Fruits'].iloc[100000:200000]
#
# # print(len(array))
#
# # pdDf = pd.read_csv('baza.csv')
# # print(pdDf)
#
#
# # test = df['Fruits'].iloc[100000:200000]
#
# # usecols = ["Fruits"]
#
# # Diabetes = pd.read_csv("baza.csv", index_col='Fruits', usecols=usecols, delimiter=',')
# # print(Diabetes.iloc[0:100000])
#
#
# #
# #
# # train = df['Fruits'].iloc[0:100000]
# # test = df['Fruits'].iloc[100000:200000]
#
# # print("test: ", test)
# # print("train: ", train)
#
# # Y_train = ["Fruits"]
# # X_train = [train]
# #
# # Y_test = ["Fruits"]
# # X_test = [test]
#
# # print("X_test: ", X_test)
# # print("X_train: ", X_train)
#
# # neigh = KNeighborsClassifier(n_neighbors=1)
# # neigh.fit(X_train, Y_train) #przyjęcie danych wejściowych oraz etykiet próbki
# # scores = neigh.predict(X_test) #prognozuje przypasowanie próbki do odpowiedniej klasy
#
# # print(accuracy_score(Y_test,scores))
#
# import math
# # results = []
# #
# # for i in range(1, 7):
# #     neigh = KNeighborsClassifier(n_neighbors=3)
# #     neigh.fit(X_train, Y_train)  # przyjęcie danych wejściowych oraz etykiet próbki
# #     scores = neigh.predict(X_test)  # prognozuje przypasowanie próbki do odpowiedniej klasy
# #     results.append(accuracy_score(Y_test, scores))
# # print("scores: ", scores)
# # print("Y_test:", Y_test)
# # print("accuracy:", accuracy_score(Y_test,scores))
# # print("results:", results)
# # print("  ")
#
# # sum(results)
# # print("sum:", round(sum(results), 2))
# #
# # avg = sum(results) / 100
# # print("avg:", round((avg), 2))
# #
# # sd_sum = 0
# # results_sum = sum(results)
# #
# # for el in results:
# #     sd_sum += (avg - el) ** 2
# # print("sd_sum:", round((sd_sum), 2))
# #
# # sd = math.sqrt(sd_sum * 0.01)
# # print("sd:", round((sd), 2))
# #
# # print("accuracy:", round(accuracy_score(Y_test, scores), 3) * 100, "%")
