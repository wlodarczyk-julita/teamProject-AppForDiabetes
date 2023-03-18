import pandas as pd
def save (array, arrayAllDate, arrayTypicalDate, name, name1, name2):
    rawDate = { name: array,
               name1: arrayAllDate,
               name2: arrayTypicalDate,
    }
    df = pd.DataFrame(rawDate, columns=[name, name1, name2])
    df.to_csv(name+'.csv', index=False, header=True)

