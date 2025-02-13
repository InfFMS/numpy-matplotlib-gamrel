# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из 100 случайных значений, где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.
while N < n - 1:  # проверка на возможности хода
    while I < 32:
        if X[I] == Xo[N] and Y[I] == Yo[N]:
            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 24 or i == 31) and 7 < I < 24:
                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                axes.add_patch(axeS)  # удар белых
            if X[I] == Xo[N] and Y[I] == Yo[N] and (i == 23 or i == 16) and (I < 8 or I > 23):
                axeS = matplotlib.patches.Circle((X[I], Y[I]), radius=0.5, fill=False, color="r")
                axes.add_patch(axeS)  # удар черных
        else:
            axeS = matplotlib.patches.Circle((Xo[N], Yo[N]), radius=0.2, fill=True, color="g")
            axes.add_patch(axeS)
        I += 1
    N += 1
    I = 0