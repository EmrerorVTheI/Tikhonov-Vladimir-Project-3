import matplotlib.pyplot as plt

from Lost import list_day, list_eu, list_us, list_cn
x = list_day
y1 = list_eu
y2 = list_us
y3 = list_cn

plt.figure(figsize=(20, 2.7))
plt.plot(x, y1, label='EU', marker='o', linewidth = 2)
manager_eu = plt.get_current_fig_manager()
manager_eu.window.move(0, 0)
plt.title('Курс Евро', fontsize = 18)
plt.xlabel('Дни', fontsize = 14)
plt.ylabel('Рубли', fontsize = 14)
plt.legend()
plt.grid(True, alpha = 0.4)
plt.tight_layout()

plt.figure(figsize=(20, 2.7))
plt.plot(x, y2, label='US', marker='s', linewidth = 2)
manager_us = plt.get_current_fig_manager()
manager_us.window.move(0, 350)
plt.title('Курс Доллара', fontsize = 18)
plt.xlabel('Дни', fontsize = 14)
plt.ylabel('Рубли', fontsize = 14)
plt.legend()
plt.grid(True, alpha = 0.4)
plt.tight_layout()

plt.figure(figsize=(20, 2.7))
plt.plot(x, y3, label='CN', marker='^', linewidth = 2)
manager_cn = plt.get_current_fig_manager()
manager_cn.window.move(0, 700)
plt.title('Курс Юаня', fontsize = 18)
plt.xlabel('Дни', fontsize = 14)
plt.ylabel('Рубли', fontsize = 14)
plt.legend()
plt.grid(True, alpha = 0.4)
plt.tight_layout()

plt.show()
