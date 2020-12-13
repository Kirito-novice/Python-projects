pole = [[0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5]
y_t=3
x_t=2
pole[y_t][x_t]='#'
pole[0][2] = '*'
pole[2][4] = '*'
y_s = 0
x_s = 0


def move():
    global x_t
    global y_t
    global d_t
    global pole
    pole[y_t][x_t] = 0
    if d_t == 'w':
        y_t -= 1
    if d_t == 'a':
        x_t -= 1
    if d_t == 's':
        y_t += 1
    if d_t == 'd':
        x_t += 1
    pole[y_t][x_t] = '#'

d_s = 0

is_shooted = False


def shoot():
    global d_s
    global is_shooted
    global y_s
    global x_s
    if is_shooted == True:
        if d_s == 'w':
            y_s -= 1
        if a == 'a':
            x_s -= 1
        if a == 'd':
            x_s += 1
        if a == 's':
            y_s += 1
        pole[y_s][x_s] = '+'




def printed(pole):
    print('', *pole[0], '\n', *pole[1], '\n', *pole[2], '\n', *pole[3], '\n', *pole[4])

printed(pole)
while True:
    a = input('Введите направление движения танка: ')
    b = input('Будем стрелять? ')
    if a == "exit":
        break
    elif a:
        d_t = a
        move()
    if b == "f":
        d_s = d_t
        is_shooted = True
        x_s = x_t
        y_s = y_t
    shoot()
    printed(pole)



