import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])

#1) 
# wrap the data above in a pandas DataFrame in a way that printing 
# the dataframe and its index and column attributes gives this result:
# (Hint: print(df);print(df.index);print(df.columns):

df = pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:])

print(df)
print(df.index)
print(df.columns)

#2) Make slices of data
#A)second column using column name
print('Second column\n',df.iloc[:,1])

#B)third column using column index (.iloc[])
print('Third column\n', df.iloc[:,2])

#C)slice element at third row of second column (use .iloc())
print('Slice element at third row of second column\n', df.iloc[2,1])
