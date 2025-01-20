import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('sales.csv')


plt.bar(df['Month'], df['Sales'], color='green', width=0.5)


plt.title('Bar Chart of Ice-cream Sales')
plt.xlabel('Month')
plt.ylabel('Sales (in thousand dollars)')


plt.show()