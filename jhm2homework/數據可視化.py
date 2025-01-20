import matplotlib.pyplot as plt
import pandas as pd



data = { 'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
         'Sales': [380,400,660,800,900,1200,1600,2200,1500,1100,600,250] }

df = pd.DataFrame(data)
df.to_csv('文件1.csv', index=False)
df = pd.read_csv('文件1.csv')


plt.bar(df['Month'], df['Sales'], color='green', width=0.5)


plt.title('Bar Chart of Ice-cream Sales')
plt.xlabel('Month')
plt.ylabel('Sales (in thousand dollars)')


plt.show()fig, ax = plt.subplots(constrained_layout=True)


bars = ax.bar(bar_labels, bar_values, color="salmon")


ax.bar_label(bars, padding=3)


ax.set_xlabel("X (unit)", fontweight="bold")
ax.set_ylabel("Y (unit)", fontweight="bold")


_ = ax.legend()

plt.show()
