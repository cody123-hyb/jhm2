import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 400)
y1 = np.sin(x)
y2 = np.cos(x)


plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.fill_between(x, y1, y2, where=(y1 > y2), color='lightblue', alpha=0.5)
plt.fill_between(x, y1, y2, where=(y1 <= y2), color='lightcoral', alpha=0.5)


plt.title('鬼脚图示例')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
