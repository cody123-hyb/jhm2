import matplotlib.pyplot as plt
import pandas as plt
import os

file_name = 'csv文件1'
if os.path.exists(file_name):
    df = pd.read_csv(file_name)

x = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Set,Oct,Nov,Dec]
y = [0,500,1000,1500,2000]
plt.plot(x,y,label='Data',color='b',marker='o')