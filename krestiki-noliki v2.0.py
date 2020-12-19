#ДОПИСАТЬ УСЛОВИЕ ДЛЯ НИЧЬИ
#ДОРАБОТАТЬ ПОВТОРНУЮ ПОПЫТКУ ЗАНЯТЬ УЖЕ ЗАНЯТУЮ КЛЕТКУ ДЛЯ 2-ого ИГРОКА

a = [['#'] * 3, ['#'] * 3, ['#'] * 3]
d = ['X'] * 3
g = ['0'] * 3
col_right = []
col_left = []
col_down1 = []
col_down2 = []
col_down3 = []
print('*' * 15, 'Игровое поле крестики-нолики', '*' * 15)
print('', *a[0], '\n', *a[1], '\n', *a[2])
for i in range(81):
    def conditions():
        for i in range(3):
            if a[i] == d:
                print('Победил игрок номер 1!')
                quit()
            if a[i] == g:
                print('Победил игрок номер 2!')
                quit()

        for i in range(3):
            col_right.append(a[i][i])
            col_left.append(a[2 - i][i])
            col_down1.append(a[i][0])
            col_down2.append(a[i][1])
            col_down3.append(a[i][2])
        #print(col_left)
        n = col_right[-3:]
        m = col_left[-3:]
        k = col_down1[-3:]
        l = col_down2[-3:]
        j = col_down3[-3:]
        #print(k, l, j)
        #print(m)
        if n == d or m == d or k == d or l == d or j == d:
            print('Победил игрок номер 1!')
            quit()
        if n == g or m == g or k == g or l == g or j == g:
            print('Победил игрок номер 2!')
            quit()

    n = list(map(int, input("Ход игрока номер 1 (Х): ").split()))
    flag = True
    if flag:
        if a[n[0] - 1][n[1] - 1] == '#':
            a[n[0] - 1][n[1] - 1] = 'X'
            flag = False
        else:
            print('Клетка уже занята!')
            print('', *a[0], '\n', *a[1], '\n', *a[2])
            continue
    print('', *a[0], '\n', *a[1], '\n', *a[2])

    conditions()

    f = list(map(int, input("Ход игрока номер 2 (0): ").split()))
    flag = True
    if flag:
        if a[f[0] - 1][f[1] - 1] == '#':
            a[f[0] - 1][f[1] - 1] = '0'
            flag = False
        else:
            print('Клетка уже занята!')
            print('', *a[0], '\n', *a[1], '\n', *a[2])
            continue
    print('', *a[0], '\n', *a[1], '\n', *a[2])












