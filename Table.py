import matplotlib.pyplot as plt
import numpy as np

from Lost import list_day, list_eu, list_us, list_cn
x = list_day
y1 = list_eu 
y2 = list_us 
y3 = list_cn
plt.figure(figsize=(9, 9))
plt.plot(x, y1, label='EU', marker='o', linewidth = 2)
plt.plot(x, y2, label='US', marker='s', linewidth = 2)
plt.plot(x, y3, label='CN', marker='^', linewidth = 2)
plt.yscale('log')
plt.title('Курс Валют', fontsize = 14)
plt.xlabel('Дни', fontsize = 12)
plt.ylabel('Рубли', fontsize = 12)
plt.legend()
plt.grid(True, alpha = 0.3)
plt.tight_layout()
plt.show()