import matplotlib.pyplot as plt
import pandas as pd
fig, ax = plt.subplots(constrained_layout=True)

# bar_labels是一个字符串列表，bar_values是一个与bar_labels等长的数字列表
# 更多参数：https://www.wolai.com/matplotlib/2mypc3HyBTyLR8TQKmxVku
bars = ax.bar(bar_labels, bar_values, color="salmon")

# 为条形添加数字标签, padding是标签与条形的距离
ax.bar_label(bars, padding=3)

data = { 'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
         'Sales': [380,400,660,800,900,1200,1600,2200,1500,1100,600,250] }

# 设置坐标轴标签
ax.set_xlabel("X (unit)", fontweight="bold")
ax.set_ylabel("Y (unit)", fontweight="bold")


# 添加图例
_ = ax.legend()

plt.show()

