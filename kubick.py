# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import matplotlib.pyplot as plt
import random
x=0
i=0
y=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
county=0
maxCount=0
contMax=0
while i<1000:
    x=random.randint(1,6)
    if i == 0:
        y=x
    if x==1:
        count1+=1
    if x==2:
        count2+=1
    if x==3:
        count3+=1
    if x==4:
        count4+=1
    if x==5:
        count5+=1
    if x==6:
        count6+=1
    i+=1
    if y == x:
        county+=1
    else:
        if maxCount<county:
            maxCount=county
            Xmax=x
        y=x
        county=0
def one(count1):
    print(1, '-', count1)
    chance1 = count1 / 10
    print(chance1, '%')
def two(count2):
    print(2, '-', count2)
    chance2 = count2 / 10
    print(chance2, '%')
def three(count3):
    print(3, '-', count3)
    chance = count3 / 10
    print(chance, '%')
def four(count4):
    print(4, '-', count4)
    chance = count4 / 10
    print(chance, '%')
def five(count5):
    print(5, '-', count5)
    chance = count5 / 10
    print(chance, '%')
def six(count6):
    print(6, '-', count6)
    chance = count6 / 10
    print(chance, '%')
one(count1)
two(count2)
three(count3)
four(count4)
five(count5)
six(count6)
print(Xmax, '-', maxCount)
plt.bar([1,2,3,4,5,6],[count1,count2,count3,count4,count5,count6])
plt.show()