import pandas as pd

df = pd.read_csv('iphone_sales_dataset.csv')
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

df['Total_Revenue'] = df['Quantity'] * df['Price'] #creating total revenue column

print (df.info())