from HighBP import informationHP

import pandas as pd
#save array as csv file
ser = pd.Series(informationHP)
ser.rename('HP', inplace=True)
ser.to_csv(r'HP.csv', index=False, header=True)
