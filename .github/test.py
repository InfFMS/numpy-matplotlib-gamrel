# Задача:# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
data = np.array([[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]])
print(data)
# Построение тепловой карты
plt.imshow(data, cmap='hot')
# Добавление цветовой шкалы
s = ["A","B","C","D","E","F","G","H"]
plt.colorbar(label="Интенсивность")
plt.xticks(range(8), labels=s)
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
circle1 = plt.Circle((3, 0), 0.2, color= "green", label="as")
ax.add_patch(circle1)
plt.legend()
fn = r'D:\prog\images.png'
im = plt.imread(fn)
ax.figure.figimage(im,
                   ax.bbox.xmax//1 - im.shape[0]//2,
                   ax.bbox.ymax//1 - im.shape[1]//2,
                   alpha=0.4, zorder=0)
plt.show()