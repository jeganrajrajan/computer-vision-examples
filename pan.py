import pandas as pd
import numpy as np

# Series
array = np.arange(1,10,2)
a =pd.Series(array)
b = pd.Series(array, index = ['val1','val2','val3','val4','val5'])
print(a)
print(b)
print(a.values)
print(a.index)

# Dictionary of key pair values called data
data = {'Roll_No':[301, 302, 303, 304, 305],
        'Age': [24, 23, 22, 19, 10]}
df = pd.DataFrame(data, index = ['anish', 'ram', 'Ashwin', 'Mohit', 'arun'])
print(df)
print(df.ndim)
print(df.shape)

# Accessing Single element
print(df.loc['ram','Age'])
print(df.iloc[4, 1])

# To get all rows
print(df.loc[:,'Age'])
print(df.loc['Ashwin', :])

# With condition
print(df.loc[lambda df: df.Age > 20, :])
# Basic Functions
read_df = pd.read_csv(r'D:\computer_vision\data\blog_dataset.csv')
print(read_df.head(10))
print(read_df.tail())
print(read_df.describe())
read_df['Gender'] = read_df.Gender.astype('category')
print(read_df)
read_df['DOB'] = pd.to_datetime(read_df['DOB'])
print(read_df['State'].value_counts())
print(read_df.drop_duplicates(inplace=True))
print(read_df.groupby(by='State').Salary.mean())


# merge
user_usage = pd.read_csv(r'D:\computer_vision\data\user_usage.csv')
user_device = pd.read_csv(r'D:\computer_vision\data\user_device.csv')
android_device =pd.read_csv(r'D:\computer_vision\data\android_devices.csv')
print(user_usage.head())
print(user_device.head())
print(android_device.head())
# left merge
left_merge = pd.merge(user_usage,user_device,on='use_id',how = 'left')
print(left_merge.head())
# right_merge
left_merge = pd.merge(user_usage,user_device,on='use_id',how = 'right')
# inner_merge
inner_merge = pd.merge(user_usage,user_device,on = 'use_id',how = 'inner')
print(inner_merge.head())
#Outer_merge
outer_merge = pd.merge(user_usage,user_device,on = 'use_id',how = 'outer',indicator = True)
# coloumn merge
left_col_merge = pd.merge(user_device,android_device,left_on = 'device',right_on = 'Model',how='left',indicator = True)
print(left_col_merge)

# sorted_val
read_df.sort_values(by='Name', inplace=True)
print(read_df)

#fillna
read_df['City temperature'].fillna(38.5, inplace=True)
print(read_df)

#concat
# importing the module
import pandas as pd

# creating the DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3']})
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],'B': ['B4', 'B5', 'B6', 'B7']})


# concatenating
print(pd.concat([df1, df2],axis = 1))
# axis =0 column
# axis = 1 row

print(pd.concat([df1, df2], ignore_index = True))
# compare
print(df1.compare(df2))



