import pandas as pd
import matplotlib.pyplot as plt


import pandas as pd

data = {
'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
'Sales': [380, 400, 660, 800, 900, 1200, 1600, 2200, 1500, 1100, 600, 250]
}
df = pd.DataFrame(data)
df.to_csv('sales.csv', index=False)


a = df['Month']
b = df['Sales']
colora = 'green'
plt.bar(a,b,color = colora,width=0.5)
plt.title("Bar Chart of ice-cream Sales")
plt.xlabel("Month")
plt.ylabel("Sales(in thousand dollars)")

plt.show()