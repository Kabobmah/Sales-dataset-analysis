import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iphone_sales_dataset.csv')

df['Total_Revenue'] = df['Quantity'] * df['Price'] #creating total revenue column

model_sales = df.groupby('iPhone_Model')['Total_Revenue'].sum().sort_values(ascending=False)

spec_sales = df.groupby(['iPhone_Model', 'Storage'])['Total_Revenue'].sum().sort_values(ascending=False).reset_index()
print("Top models by margin:")

print(model_sales)
print ('-----------------------------------------------------------------------------------------------------------------------------------------------')
print("Top configs by margin:")

print(spec_sales.head(30))
plt.figure(figsize=(12, 6))
sns.barplot(data=spec_sales, x='Total_Revenue', y='iPhone_Model', hue='Storage')
plt.title('Margin of Model/Storage size')
plt.xlabel('Total value ($)')
plt.ylabel('iPhone Model')
plt.legend(title='Storage', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

