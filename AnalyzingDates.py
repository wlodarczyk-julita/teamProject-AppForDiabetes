# import Fruits
# import Diabetes
# import LoadDate
#
# print('**************DIABETES**************')
# print('No diabetes', Diabetes.no_diabetes)
# print('Prediabetes ', Diabetes.prediabetes)
# print('Diabetes', Diabetes.diabetes)
#
# print('\n**************FRUITS**************')
# print('No diabetes no fruits', Fruits.zero_zero)
# print('No diabetes + fruits', Fruits.zero_one)
# print('Prediabetes no fruits', Fruits.one_zero)
# print('Prediabetes + fruits', Fruits.one_one)
# print('Diabetes no fruits', Fruits.two_zero)
# print('Diabetes + fruits', Fruits.two_one)
#
# #print('\nCheck', zero_zero + one_zero + two_zero + zero_one + one_one + two_one)
#
#
# print('\nPercent analyzing all date: ')
# print('No diabetes no fruits', LoadDate.percent_value(Fruits.zero_zero, LoadDate.countDiabetes), '%')
# print('No diabetes + fruits', LoadDate.percent_value(Fruits.zero_one, LoadDate.countDiabetes), '%')
# print('Prediabetes no fruits', LoadDate.percent_value(Fruits.one_zero, LoadDate.countDiabetes), '%')
# print('Prediabetes + fruits', LoadDate.percent_value(Fruits.one_one, LoadDate.countDiabetes), '%')
# print('Diabetes no fruits', LoadDate.percent_value(Fruits.two_zero, LoadDate.countDiabetes), '%')
# print('Diabetes + fruits', LoadDate.percent_value(Fruits.two_one, LoadDate.countDiabetes), '%')
#
# print('\nPercent analyzing No diabetes: ')
# print('No diabetes no fruits', LoadDate.percent_value(Fruits.zero_zero, Diabetes.no_diabetes), '%')
# print('No diabetes + fruits', LoadDate.percent_value(Fruits.zero_one, Diabetes.no_diabetes), '%')
#
# print('\nPercent analyzing Prediabetes: ')
# print('Prediabetes no fruits', LoadDate.percent_value(Fruits.one_zero, Diabetes.prediabetes), '%')
# print('Prediabetes + fruits', LoadDate.percent_value(Fruits.one_one, Diabetes.prediabetes), '%')
#
# print('\nPercent analyzing Diabetes: ')
# print('Diabetes no fruits', LoadDate.percent_value(Fruits.two_zero, Diabetes.diabetes), '%')
# print('Diabetes + fruits', LoadDate.percent_value(Fruits.two_one, Diabetes.diabetes), '%')
#
# print('\n**************HP**************')
# print('No diabetes no HP', zero_zeroHP)
# print('No diabetes + HP', zero_oneHP)
# print('Prediabetes no HP', one_zeroHP)
# print('Prediabetes + HP', one_oneHP)
# print('Diabetes no HP', two_zeroHP)
# print('Diabetes + HP', two_oneHP)
#
# print('\nPercent analyzing No diabetes: ')
# print('No diabetes no HP', LoadDate.percent_value(zero_zeroHP, Diabetes.no_diabetes), '%')
# print('No diabetes + HP', LoadDate.percent_value(zero_oneHP, Diabetes.no_diabetes), '%')
#
# print('\nPercent analyzing Prediabetes: ')
# print('Prediabetes no HP', LoadDate.percent_value(one_zeroHP, Diabetes.prediabetes), '%')
# print('Prediabetes + HP', LoadDate.percent_value(one_oneHP, Diabetes.prediabetes), '%')
#
# print('\nPercent analyzing Diabetes: ')
# print('Diabetes no HP', LoadDate.percent_value(two_zeroHP, Diabetes.diabetes), '%')
# print('Diabetes + HP', LoadDate.percent_value(two_oneHP, Diabetes.diabetes), '%')
#
