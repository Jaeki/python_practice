import pandas as pd
import numpy as np

exam_data = {'name':['Anastasia', 'Catherine', 'Cohill', 'James', 'Emily', 'Michael', 'Monica', 'Laura', 'Kevin', 'Jordan'],
             'score':[13,9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
             'attempts':[1,3,3,2,2,3,2,3,2,1],
             'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels=['a', 'b', 'c', 'd', 'e', 'f','g', 'h','i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print(df)

#1-1 select 'name' and 'score' columns
print(df[['name','score']])

#1-2
print(df.head(3))
print(df.iloc[:3])
print(df.loc['a':'c'])

#1-3
print(df[['name','score']].iloc[[1,2,5,6]])

#1-4
print(df[df['attempts']>2])


#2-1
print(df[df['score'].isnull()==True])

