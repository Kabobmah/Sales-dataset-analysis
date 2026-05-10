import pandas as pd

df = pd.read_csv('iphone_sales_dataset.csv')

print(df.head()) #looking at first 5 lines of the file 
print('___________________________________________')
print(df.info()) 
print(df['Price'].describe())