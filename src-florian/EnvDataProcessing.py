'''
Created on 17.06.2019

@author: fkluiben
'''
#check for eclipse + github tutorial https://www.youtube.com/watch?reload=9&v=XuuzSaelUzo

#import numpy as np

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose


import matplotlib.pyplot as plt
import os

os.chdir(os.environ['PROJECT_PATH'])

# myPath = os.path.join(os.getcwd(),"..\\Data\\smhi-opendata_5_53540_20190617_233641.csv")

# print(myPath)

dfP = pd.read_csv("Data/smhi-opendata_5_53540_20190617_233641.csv" , skiprows=10, usecols=[2, 3, 4], sep=";")
dfP.columns = ["Day", "P", "Quality"]


dfP = dfP.set_index("Day")
#make sure that index is datetime (convenient for time series=
dfP.index = pd.to_datetime(dfP.index)
#p = dfP["P"]
dfP.isnull().sum() # see if there is any missing data
dfP.dtypes

# now access and slicing is easy...
#print(dfP.loc['2000-6-1':'2000-6-10'])

#resample mostly used for time series data...check

dfP1 = dfP.resample("M").sum()
#dfP1.loc["2012-06"]
p = dfP1["P"]


result = seasonal_decompose(p, model='additive')
result.plot()
# plt.plot(result)
plt.show()



plt.plot(dfP1)
plt.show()  # You must call plt.show() to make graphics appear.
print("Did it plot?")

