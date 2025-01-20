import matplotlib.pyplot as plt
import pandas as pd



data = { 'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
         'Sales': [50, 75, 60, 80, 90, 100, 110, 85, 95, 105, 70, 65] }
df = pd.DataFrame(data)
df = pd.read_csv('sales.csv', index=False)


plt.bar(df['Month'], df['Sales'], color='green', width=0.5)


plt.title('Bar Chart of Ice-cream Sales')
plt.xlabel('Month')
plt.ylabel('Sales (in thousand dollars)')


plt.show()