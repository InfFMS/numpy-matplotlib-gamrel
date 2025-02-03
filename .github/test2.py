import matplotlib.pyplot as plt
import numpy as np
import random
pv=np.zeros((10, 10))
pv_show=np.zeros((10, 10))
i=0
Y=[0]
X=[0]
n=0
while i<16:
    x = (random.randint(0, 9))
    y = (random.randint(0, 9))
    n=0
    while n<len(X):
        if x!=X[n] and y!=Y[n]:
            X.append(x)
            Y.append(y)
            n+=30
        n+=1
    if n<20:
        i-=1
    i+=1
    if i == 1:
        del X[0] #иногда лагает, но крайне редко. просто перезапустите
        del Y[0]
i=0
while i<15:
    x=X[i]
    y=Y[i]
    pv[x,y]=8
    i+=1
n=0
x=0
y=0
while x<10:
    while y < 10:
        if pv[x,y]==0:
            Q=0
            q = x
            w = y
            if x!=0 and x!=9:
                q-=1
            if y!=0 and y!=9:
                w-=1
            I = 0
            i1=0
            if x == 0:
                I+=1
            if x == 9:
                q -= 1
                I += 1
            if y == 0:
                i1=1
            if y == 9:
                i1=1
                w -= 1
            i = i1
            counter=0
            while I<3:
                while i<3:
                    if pv[q,w]==8:
                        counter+=1
                    w+=1
                    i+=1
                    Q+=1
                i=i1
                w-=Q
                q+=1
                I+=1
                Q=0
            if counter>0:
                pv[x,y]+=counter
            if counter == 0:
                pv[x, y] += 7
        y+=1
    y=0
    x+=1
#print (pv)
q=0
k=15
n=0
score=0
while score<15:
    plt.imshow(pv_show, cmap='hot')
    plt.colorbar(label="значение")
    plt.show()
    print(pv_show)
    print ("Введите 8 чтобы поставить флажок")
    print("Введите 0 чтобы убрать флажок")
    print("флажков осталось:", k)
    print("Введите число != {8, 0}, указать клетку для открытия ")
    z=int(input())
    if z !=8:
        print ("Укажите x:")
        y=int(input())
        print ("Уккажите y:")
        x=int(input())
        if pv[x,y] != 8:
            pv_show[x,y]+=pv[x,y]
            one = plt.Rectangle((y, x), 1, 1, linewidth=1, edgecolor='b', facecolor='none')
        elif pv[x,y] == 8:
            score+=100
        if pv[x, y] == 7:
            Q = 0
            q = x
            w = y
            if x != 0 and x != 9:
                q -= 1
            if y != 0 and y != 9:
                w -= 1
            I = 0
            i1 = 0
            if x == 0:
                I += 1
            if x == 9:
                q -= 1
                I += 1
            if y == 0:
                i1 = 1
            if y == 9:
                i1 = 1
                w -= 1
            i = i1
            counter = 0
            while I < 3:
                while i < 3:
                    pv_show[q, w] = pv[q,w]
                    w += 1
                    i += 1
                    Q += 1
                i = i1
                w -= Q
                q += 1
                I += 1
                Q = 0
    if z==8 and k>0:
        print ("Укажите x:")
        y=int(input())
        print ("Уккажите y:")
        x=int(input())
        pv_show[x,y]=9
        k-=1
        if pv[y,x]==8:
            score+=1
    if z == 8 and k < 0:
        print("недостаточно флажков")
    if z==0:
        print ("Укажите x:")
        y=int(input())
        print ("Уккажите y:")
        x=int(input())
        if pv_show[y,x]==9:
            pv_show[y,x]=0
            k+=1
            if pv[y, x] == 8:
                score -= 1
        else:
            print("У вас нет флажка на:", '[', x, y, ']')
if score==15:
    print ("you win!!")
else:
    print ("you lose")
    print(pv)
    plt.imshow(pv, cmap='hot')
    plt.show()