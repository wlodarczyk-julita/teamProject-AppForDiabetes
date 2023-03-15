import numpy as np
import pandas as pd
import csv

import LoadDate

prediabetes  = 0
diabetes = 0
no_diabetes = 0
for i in range(LoadDate.countDiabetes):
    if LoadDate.arrayDiabetes[i] == 0.0: no_diabetes = no_diabetes + 1
    if LoadDate.arrayDiabetes[i] == 1.0: prediabetes = prediabetes + 1
    if LoadDate.arrayDiabetes[i] == 2.0: diabetes = diabetes + 1


