import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [380, 400, 660, 800, 900, 1200, 1600, 2200, 1500, 1100, 600, 250]
colara = ['green']
plt.bar(x,y , colar = colara)
plt.title("Bar Chart of ice-cream Sales")
plt.xlabel("Month")
plt.ylabel("Sales(in thousand dollars)")
plt.xticks(x, ["Jan","feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
plt.show()