# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches
import matplotlib.path
import re
y=0
x=0
pv=np.zeros((8, 8))
while y<8:
    while x < 8:
        pv[x,y]=1
        x += 2
    y+=1
    if y%2==0:
        x=0
    else:
        x=1
S = ["A","B","C","D","E","F","G","H"]
s = ["a","b","c","d","e","f","g","h"]
plt.xticks(range(8), labels=s)
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
N=0
Nt=0
N1=0
stop1=0
stop2=0
I=0
n=1
i=0
x=0
x1=0
X=[]
y=0
Y=[]
Xo=[]
Yo=[]
count=0
i1=0
#фигуры
while i<8:
    y=6
    Y.append(y)
    X.append(x)
    x+=1
    i+=1 #i [0,7] - пешки
x=0
while i<16:
    y=1
    Y.append(y)
    X.append(x)
    x+=1
    i+=1 #i [8,15] черные пешки
x=0
while i<24:
    y=0
    Y.append(y)
    X.append(x)
    x+=1
    i+=1 #i [16, 23] черные фигуры 16, 23 - ладьи. 17, 22 - кони, 18, 21 - слоны, 19 - ферзь, 20 - король
x=0
while i<32:
    y=7
    Y.append(y)
    X.append(x)
    x+=1
    i+=1 #i [24,31] белые фигуры 24, 31 - ладьи. 25, 30 - кони, 26, 29 - слоны, 27 - ферзь, 28 - король
while X[20]!=11 or X[28]!=11:
    if i==0: #просто чтобы красиво свернуть
        i=27
        plt.text(X[i], Y[i], "Кф", color="g")
        i = 19
        plt.text(X[i], Y[i], "Кф", color="r")
        i =24
        plt.text(X[i], Y[i], "Л", color="g")
        i = 31
        plt.text(X[i], Y[i], "л", color="g")
        i = 25
        plt.text(X[i], Y[i], "К", color="g")
        i = 30
        plt.text(X[i], Y[i], "К", color="g")
        i = 0
        plt.text(X[i], Y[i], "п", color="g")
        i = 1
        plt.text(X[i], Y[i], "п", color="g")
        i = 2
        plt.text(X[i], Y[i], "п", color="g")
        i = 3
        plt.text(X[i], Y[i], "п", color="g")
        i = 4
        plt.text(X[i], Y[i], "п", color="g")
        i = 5
        plt.text(X[i], Y[i], "п", color="g")
        i = 6
        plt.text(X[i], Y[i], "п", color="g")
        i = 7
        plt.text(X[i], Y[i], "п", color="g")
        i = 16
        plt.text(X[i], Y[i], "Л", color="r")
        i = 23
        plt.text(X[i], Y[i], "л", color="r")
        i = 17
        plt.text(X[i], Y[i], "К", color="r")
        i = 22
        plt.text(X[i], Y[i], "К", color="r")
        i = 8
        plt.text(X[i], Y[i], "п", color="r")
        i = 9
        plt.text(X[i], Y[i], "п", color="r")
        i = 10
        plt.text(X[i], Y[i], "п", color="r")
        i = 11
        plt.text(X[i], Y[i], "п", color="r")
        i = 12
        plt.text(X[i], Y[i], "п", color="r")
        i = 13
        plt.text(X[i], Y[i], "п", color="r")
        i = 14
        plt.text(X[i], Y[i], "п", color="r")
        i = 15
        plt.text(X[i], Y[i], "п", color="r")
    plt.imshow(pv, cmap='hot')
    plt.show()
    print ("Укажите фигуру")
    H=str(input())
    y1=int(H[0])
    y1=8-y1
    x1=H[1]
    i=0
    #перевод из буквенного в числовое обозначение
    while i<8:
        if s[i]==x1 or S[i]==x1:
            x1=i
            i+=10
        i+=1
    i=0
    if i == 0:  # просто чтобы красиво свернуть
        i = 27
        plt.text(X[i], Y[i], "Кф", color="g")
        i = 19
        plt.text(X[i], Y[i], "Кф", color="r")
        i = 24
        plt.text(X[i], Y[i], "Л", color="g")
        i = 31
        plt.text(X[i], Y[i], "л", color="g")
        i = 25
        plt.text(X[i], Y[i], "К", color="g")
        i = 30
        plt.text(X[i], Y[i], "К", color="g")
        i = 0
        plt.text(X[i], Y[i], "п", color="g")
        i = 1
        plt.text(X[i], Y[i], "п", color="g")
        i = 2
        plt.text(X[i], Y[i], "п", color="g")
        i = 3
        plt.text(X[i], Y[i], "п", color="g")
        i = 4
        plt.text(X[i], Y[i], "п", color="g")
        i = 5
        plt.text(X[i], Y[i], "п", color="g")
        i = 6
        plt.text(X[i], Y[i], "п", color="g")
        i = 7
        plt.text(X[i], Y[i], "п", color="g")
        i = 16
        plt.text(X[i], Y[i], "Л", color="r")
        i = 23
        plt.text(X[i], Y[i], "л", color="r")
        i = 17
        plt.text(X[i], Y[i], "К", color="r")
        i = 22
        plt.text(X[i], Y[i], "К", color="r")
        i = 8
        plt.text(X[i], Y[i], "п", color="r")
        i = 9
        plt.text(X[i], Y[i], "п", color="r")
        i = 10
        plt.text(X[i], Y[i], "п", color="r")
        i = 11
        plt.text(X[i], Y[i], "п", color="r")
        i = 12
        plt.text(X[i], Y[i], "п", color="r")
        i = 13
        plt.text(X[i], Y[i], "п", color="r")
        i = 14
        plt.text(X[i], Y[i], "п", color="r")
        i = 15
        plt.text(X[i], Y[i], "п", color="r")
    i = 0
    plt.xticks(range(8), labels=s)
    plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
    axes = plt.gca()
    axeS=matplotlib.patches.Circle((x1, y1), radius=0.5, fill=False, color="g")
    axes.add_patch(axeS)
    while i<32:
        if X[i]==x1 and Y[i]==y1:
            i1=i
            #изменить размер зеленых кружочков
            # ходы белых пешек
            if i<8:
                Xo.append(x1)
                Yo.append(y1-1)
                Yo.append(y1-2)
                xb1 = 0;xb2 = 0;yb=1
                if x1<7:
                    xb1=x1+1
                else: stop1=1
                if x1>0:
                    xb2=x1-1
                else:
                    stop2=1
                yb=y1-1
                while I < 32:#проверка на возможности хода
                    if X[I] == x1 and Y[I] == y1-1:
                        count+=2
                    if X[I] == x1 and Y[I] == y1 - 2 and count<2:
                        count += 1
                    if X[I] == xb1 and Y[I] == yb and stop1!=1 and 7<I<24:
                        axeS=matplotlib.patches.Circle((xb1, yb),radius=0.5,fill=False,color="r")
                        axes.add_patch(axeS)
                    if X[I] == xb2 and Y[I] == yb and stop2!=1 and 7<I<24:
                        axeS=matplotlib.patches.Circle((xb2, yb), radius=0.5, fill=False, color="r")
                        axes.add_patch(axeS)
                    I += 1
                if count==0:
                    if y1 > 0:
                        axeS=matplotlib.patches.Circle((Xo[0], Yo[0]), radius=0.2, fill=True, color="g")
                        axes.add_patch(axeS)
                    if y1 > 1:
                        axeS=matplotlib.patches.Circle((Xo[0], Yo[1]), radius=0.2, fill=True, color="g")
                        axes.add_patch(axeS)
                if count == 1 and y1 > 0:
                    axeS=matplotlib.patches.Circle((Xo[0], Yo[0]), radius=0.2, fill=True, color="g")
                    axes.add_patch(axeS)
                I = 0
                Xo=[]
                Yo=[]
                stop1=0
                stop2=0
            # ходы черных пешек
            if 7<i<16:
                Xo.append(x1)
                Yo.append(y1+1)
                Yo.append(y1+2)
                xb1 = 0;xb2 = 0;yb=1
                if x1<7:
                    xb1=x1+1
                else: stop1=1
                if x1>0:
                    xb2=x1-1
                else:
                    stop2=1
                yb=y1+1
                while I < 32:#проверка на возможности хода
                    if X[I] == x1 and Y[I] == y1+1:
                        count+=2
                    if X[I] == x1 and Y[I] == y1 + 2 and count<2:
                        count += 1
                    if X[I] == xb1 and Y[I] == yb and stop1!=1 and (I<8 or I>23):
                        axeS=matplotlib.patches.Circle((xb1, yb),radius=0.5,fill=False,color="r")
                        axes.add_patch(axeS)
                    if X[I] == xb2 and Y[I] == yb and stop2!=1 and (I<8 or I>23):
                        axeS=matplotlib.patches.Circle((xb2, yb), radius=0.5, fill=False, color="r")
                        axes.add_patch(axeS)
                    I += 1
                if count==0:
                    if y1 < 8:
                        axeS=matplotlib.patches.Circle((Xo[0], Yo[0]), radius=0.2, fill=True, color="g")
                        axes.add_patch(axeS)
                    if y1 < 7:
                        axeS=matplotlib.patches.Circle((Xo[0], Yo[1]), radius=0.2, fill=True, color="g")
                        axes.add_patch(axeS)
                if count == 1 and y1 < 8:
                    axeS=matplotlib.patches.Circle((Xo[0], Yo[0]), radius=0.2, fill=True, color="g")
                    axes.add_patch(axeS)
                I = 0
                Xo = []
                Yo = []
            #ладьи
            if i==16 or i== 31 or i == 24 or i == 23:
                while x1+n < 8:
                    Xo.append(x1+n)
                    n+=1
                while N<n-1:#проверка на возможности хода
                    while I < 32 and N<n-1:
                        if X[I] == Xo[N] and Y[I] == y1:
                            if X[I] == Xo[N] and Y[I] == y1 and (i==24 or i ==31) and 7<I<24 :
                                axeS = matplotlib.patches.Circle((Xo[N], y1), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS) #удар белых
                            if X[I] == Xo[N] and Y[I] == y1 and (i==23 or i ==16) and (I<8 or I>23):
                                axeS = matplotlib.patches.Circle((Xo[N], y1), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS) #удар черных
                            n -= 33
                        if X[I] != Xo[N] or Y[I] != y1:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], y1), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
                N = 0
                n = 1
                Xo = []
                while x1 - n > -1:
                    Xo.append(x1 - n)
                    n += 1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == y1:
                            if X[I] == Xo[N] and Y[I] == y1 and (i == 24 or i == 31) and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((Xo[N], y1), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == y1 and (i == 23 or i == 16) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((Xo[N], y1), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if X[I] != Xo[N] or Y[I] != y1:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], y1), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
                N = 0
                n = 1
                Xo = []
                while y1-n >-1:
                    Yo.append(y1-n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == x1 and Y[I] == Yo[N]:
                            if X[I] == x1 and Y[I] == Yo[N] and (i == 24 or i == 31) and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == x1 and Y[I] == Yo[N] and (i == 23 or i == 16) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if X[I] != x1 or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((x1, Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
                N = 0
                n = 1
                Yo = []
                while y1+n < 8:
                    Yo.append(y1+n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == x1 and Y[I] == Yo[N]:
                            if X[I] == x1 and Y[I] == Yo[N] and (i == 24 or i == 31) and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == x1 and Y[I] == Yo[N] and (i == 23 or i == 16) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if  X[I] != x1 or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((x1, Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
                N = 0
                n = 1
                Yo = []
            # слоны
            if i == 18 or i == 21 or i == 26 or i == 29:
                while x1+n < 8 and y1+n < 8:
                    Xo.append(x1+n)
                    Yo.append(y1 + n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 26 or i == 29) and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 18 or i == 21) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                                n-=33
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count=0
                    N1=0
                N=0
                n=1
                Xo = []
                Yo=[]
                while x1-n > -1 and y1-n > -1:
                    Xo.append(x1-n)
                    Yo.append(y1-n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 26 or i == 29) and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 18 or i == 21) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    count = 0
                    N1 = 0
                    N += 1
                    I = 0
                    if count == 1:
                        axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.3, fill=True, color="g")
                        axes.add_patch(axeS)
                    count = 0
                n = 1
                N=0
                I = 0
                Xo = []
                Yo = []
                while x1+n < 8 and y1-n > -1:
                    Xo.append(x1+n)
                    Yo.append(y1-n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 26 or i == 29) and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 18 or i == 21) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n=0
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    count = 0
                    N1 = 0
                    N += 1
                    I = 0
                    if count == 1:
                        axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.3, fill=True, color="g")
                        axes.add_patch(axeS)
                    count = 0
                n = 1
                N=0
                I = 0
                Xo = []
                Yo = []
                while x1-n > -1 and y1+n < 8:
                    Xo.append(x1-n)
                    Yo.append(y1+n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 26 or i == 29) and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 18 or i == 21) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n-=33
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    count = 0
                    N1 = 0
                    N += 1
                    I = 0
                    if count == 1:
                        axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.3, fill=True, color="g")
                        axes.add_patch(axeS)
                    count = 0
                n = 1
                N=0
                I = 0
                Xo = []
                Yo = []
            # ферзи
            if i == 19 or i == 27:
                while x1 + n < 8:
                    Xo.append(x1 + n)
                    n += 1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == y1:
                            if X[I] == Xo[N] and Y[I] == y1 and i == 27 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((Xo[N], y1), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == y1 and (i == 19) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((Xo[N], y1), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if X[I] != Xo[N] or Y[I] != y1:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], y1), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
                N = 0
                n = 1
                Xo = []
                while x1 - n > -1:
                    Xo.append(x1 - n)
                    n += 1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == y1:
                            if X[I] == Xo[N] and Y[I] == y1 and i == 27 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((Xo[N], y1), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == y1 and (i == 19) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((Xo[N], y1), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if X[I] != Xo[N] or Y[I] != y1:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], y1), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
                N = 0
                n = 1
                Xo = []
                while y1 - n > -1:
                    Yo.append(y1 - n)
                    n += 1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == x1 and Y[I] == Yo[N]:
                            if X[I] == x1 and Y[I] == Yo[N] and i == 27 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((x1, Yo[N]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == x1 and Y[I] == Yo[N] and (i == 19) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle( (x1, Yo[N]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if X[I] != x1 or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((x1, Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
                N = 0
                n = 1
                Yo = []
                while y1 + n < 8:
                    Yo.append(y1 + n)
                    n += 1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == x1 and Y[I] == Yo[N]:
                            if X[I] == x1 and Y[I] == Yo[N] and i == 27 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == x1 and Y[I] == Yo[N] and i == 19 and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if X[I] != x1 or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((x1, Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
                N = 0
                n = 1
                Yo = []
                while x1+n < 8 and y1+n < 8:
                    Xo.append(x1+n)
                    Yo.append(y1 + n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 27 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 19 and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                                n-=33
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    N += 1
                    I = 0
                    count=0
                    N1=0
                N=0
                n=1
                Xo = []
                Yo=[]
                while x1-n > -1 and y1-n > -1:
                    Xo.append(x1-n)
                    Yo.append(y1-n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 27 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 19 and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n -= 33
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    count = 0
                    N1 = 0
                    N += 1
                    I = 0
                    if count == 1:
                        axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.3, fill=True, color="g")
                        axes.add_patch(axeS)
                    count = 0
                n = 1
                N=0
                I = 0
                Xo = []
                Yo = []
                while x1+n < 8 and y1-n > -1:
                    Xo.append(x1+n)
                    Yo.append(y1-n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 27 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 19 and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n=0
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    count = 0
                    N1 = 0
                    N += 1
                    I = 0
                    if count == 1:
                        axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.3, fill=True, color="g")
                        axes.add_patch(axeS)
                    count = 0
                n = 1
                N=0
                I = 0
                Xo = []
                Yo = []
                while x1-n > -1 and y1+n < 8:
                    Xo.append(x1-n)
                    Yo.append(y1+n)
                    n+=1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32 and N < n - 1:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 27 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 19 and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                            n-=33
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        if count == 32:
                            axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                            axes.add_patch(axeS)
                        I += 1
                    count = 0
                    N1 = 0
                    N += 1
                    I = 0
                    if count == 1:
                        axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.3, fill=True, color="g")
                        axes.add_patch(axeS)
                    count = 0
                n = 1
                N=0
                I = 0
                Xo = []
                Yo = []
            # кони
            if i == 17 or i == 22 or i == 25 or i == 30:
                if y1<6 and x1!=0:
                    Xo.append(x1+1)
                    Yo.append(y1+2)
                    n+=1
                if y1<6 and x1!=7:
                    Xo.append(x1-1)
                    Yo.append(y1+2)
                    n += 1
                if y1>1 and x1!=0:
                    Xo.append(x1+1)
                    Yo.append(y1-2)
                    n += 1
                if y1>1 and x1!=7:
                    Xo.append(x1-1)
                    Yo.append(y1-2)
                    n += 1
                if y1!=0 and x1<6:
                    Xo.append(x1+2)
                    Yo.append(y1-1)
                    n += 1
                if y1!=0 and x1>1:
                    Xo.append(x1-2)
                    Yo.append(y1-1)
                    n += 1
                if y1!=7 and x1<6:
                    Xo.append(x1+2)
                    Yo.append(y1+1)
                    n += 1
                if y1!=7 and x1>1:
                    Xo.append(x1-2)
                    Yo.append(y1+1)
                    n += 1
                while N < n-1:  # проверка на возможности хода
                    while I < 32:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 25 or i == 30) and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 17 or i == 22) and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                        if X[I]!=Xo[N] or Y[I] != Yo[N]:
                            count+=1
                            N1=N
                        I += 1
                    if count==32:
                        axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                        axes.add_patch(axeS)
                    N += 1
                    I = 0
                    count=0
                    N1=0
            # король
            if i == 20 or i == 28:
                if y1!=7 and x1!=0:
                    Xo.append(x1-1)
                    Yo.append(y1+1)
                    n+=1
                if y1!=7:
                    Xo.append(x1)
                    Yo.append(y1+1)
                    n += 1
                if y1!=7 and x1!=7:
                    Xo.append(x1+1)
                    Yo.append(y1+1)
                    n += 1
                if y1 != 0 and x1 != 0:
                    Xo.append(x1 - 1)
                    Yo.append(y1 - 1)
                    n += 1
                if y1 != 0:
                    Xo.append(x1)
                    Yo.append(y1 - 1)
                    n += 1
                if y1 != 0 and x1 != 7:
                    Xo.append(x1 + 1)
                    Yo.append(y1 - 1)
                    n += 1
                if  x1!=0:
                    Xo.append(x1-1)
                    Yo.append(y1)
                    n += 1
                if x1 != 8:
                    Xo.append(x1+1)
                    Yo.append(y1)
                    n += 1
                while N < n - 1:  # проверка на возможности хода
                    while I < 32:
                        if X[I] == Xo[N] and Y[I] == Yo[N]:
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 28 and 7 < I < 24:
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар белых
                            if X[I] == Xo[N] and Y[I] == Yo[N] and i == 20 and (I < 8 or I > 23):
                                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                                axes.add_patch(axeS)  # удар черных
                        if X[I] != Xo[N] or Y[I] != Yo[N]:
                            count += 1
                            N1 = N
                        I += 1
                    if count == 32:
                        axeS = matplotlib.patches.Circle((Xo[N1], Yo[N1]), radius=0.2, fill=True, color="g")
                        axes.add_patch(axeS)
                    N += 1
                    I = 0
                    count = 0
                    N1 = 0
        i += 1
    plt.imshow(pv, cmap='hot')
    plt.show()
    print ("Укажите ход")
    H=str(input())
    y2=int(H[0])
    y2=8-y2
    x2=H[1]
    i=0
    #перевод из буквенного в числовое обозначение
    while i<8:
        if s[i]==x2 or S[i]==x2:
            x2=i
            i+=10
        i+=1
    I=0
    count=0
    while I<32:
        if X[I]!=x2 or Y[I]!=y2:
            count+=1
        else:
            X[I]=11
            Y[I]=11
            X[i1] = x2
            Y[i1] = y2
        if count==32:
            X[i1] = x2
            Y[i1] = y2
        I+=1
    I=0
    count=0
    i=0
#конец