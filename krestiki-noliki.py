a = [0] * 3
b = [0] * 3
c = [0] * 3
d = [1] * 3
g = [2] * 3
print('*' * 15, 'Игровое поле крестики-нолики', '*' * 15)
print('', *a, '\n', *b, '\n', *c)
for i in range(81): # НЕ ЗАБЫТЬ НАПИСАТЬ УСЛОВИЕ ДЛЯ ПОБЕДЫ ИГРОКА ИЛИ ПОПЫТКИ ВВЕСТИ ЗНАЧЕНИЕ НА УЖЕ ЗАНЯТУЮ ПОЗИЦИЮ!!!!

    if ((a or b or c) == d) or ((a or b or c) == g) or (a[0] and b[1] and c[2] == (1 or 2)) or (a[2] and b[1] and c[0] == (1 or 2)) or ((a[0] and b[0] and c[0] == (1 or 2)) or (a[1] and b[1] and c[1] == (1 or 2)) or (a[2] and b[2] and c[2] == (1 or 2))):
        if ((a or b or c) == d) or (a[0] and b[1] and c[2] == 1) or (a[2] and b[1] and c[0] == 1) or (a[0] and b[0] and c[0] == 1) or (a[1] and b[1] and c[1] == 1) or (a[2] and b[2] and c[2] == 1):
            print('Игрок номер 1 победил, поздравляем!')
            exit()
        elif ((a or b or c) == g) or (a[0] and b[1] and c[2] == 2) or (a[2] and b[1] and c[0] == 2) or ((a[0] and b[0] and c[0] == 2) or (a[1] and b[1] and c[1] == 2) or (a[2] and b[2] and c[2] == 2)):
            print('Игрок номер 2 победил, поздравляем!')
            exit()
        else:
            print('Игра окончилась в ничью, поздравляем!')
            exit()

    elif ((a or b or c) != d) or ((a or b or c) != g) or (a[0] != b[1] != c[2] != (1 or 2)) or (a[2] != b[1] != c[0] != (1 or 2)) or ((a[0] and b[0] and c[0] != (1 or 2)) or (a[1] and b[1] and c[1] != (1 or 2)) or (a[2] and b[2] and c[2] != (1 or 2))):
        n = list(map(int, input('Ход игрока номер 1. Введите номер строки (от 1 до 3) и номер позиции "X" (от 0 до 2): ').split()))
        if n[0] == 1 and a[n[1]] != (1 or 2):
            a[n[1]] = 1
            print('', *a, '\n', *b, '\n', *c)
        elif n[0] == 2 and b[n[1]] != (1 or 2):
            b[n[1]] = 1
            print('', *a, '\n', *b, '\n', *c)
        elif n[0] == 3 and c[n[1]] != (1 or 2):
            c[n[1]] = 1
            print('', *a, '\n', *b, '\n', *c)

        f = list(map(int, input('Ход игрока номер 2. Введите номер строки (от 1 до 3) и номер позиции "O" (от 0 до 2): ').split()))
        if f[0] == 1 and a[f[1]] != (1 or 2):
            a[f[1]] = 2
            print('', *a, '\n', *b, '\n', *c)
        elif f[0] == 2 and b[f[1]] != (1 or 2):
            b[f[1]] = 2
            print('', *a, '\n', *b, '\n', *c)
        elif f[0] == 3 and c[f[1]] != (1 or 2):
            c[f[1]] = 2
            print('', *a, '\n', *b, '\n', *c)





