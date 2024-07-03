import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

#read data from ods
all_data = pd.read_excel('data_2_thread_max_to_node.ods')
data = all_data['div'].dropna().to_numpy()
text = all_data['node rus'].dropna().to_numpy()
x_name = "knot"
y_name = "tens.str. without a knot to the tens.str. with a knot, %"

# Строим гистограмму
bars = plt.bar(range(len(data)), data, color='skyblue', edgecolor='black')

# Добавляем подписи к каждому столбцу
i=0
for bar, value in zip(bars, data):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), text[i], ha='center', va='bottom')
    i=i+1

# Добавляем заголовок и метки осей
plt.title('2 node, d = 0.7 mm, lavsan')
plt.xlabel(x_name)
plt.ylabel(y_name)

# Отображаем гистограмму
#plt.show()
plt.savefig("data_2_thread_max_to_node.png")
