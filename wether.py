# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import matplotlib.pyplot as plt
import random
from collections import Counter
x=[]
y=[]
xs=[]
I=0
i=1
X=0
county=0
maxCount=0
while i<366:
    I+=1
    y.append(I)
    X=(random.randint(-31,29))
    x.append(X)
    i+=1
    if X < 0:
        county+=1
    else:
        if maxCount<county:
            maxCount=county
        county=0
i=-31
plt.bar(y,x)
x=sorted(x)
counts = Counter(x)
print(counts)
print(counts[1])
while i < 30:
    xs.append(counts[i])
    i+=1
countsx=sorted(counts, key=None, reverse=False)
print(countsx)
print(xs)
print(maxCount)
plt.show()
plt.bar(countsx,xs)
plt.show()