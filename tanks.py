pole = [[0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5]
y_t=3
x_t=2
pole[y_t][x_t]='^'
pole[1][2] = '*'
pole[2][4] = '*'
y_s = 0
x_s = 0

#Доделать выстрел!
import threading
import time


is_moving = False
def move():
    global x_t
    global y_t
    global d_t
    global pole
    global is_moving
    if is_moving:
        pole[y_t][x_t] = 0
        if d_t == 'w':
            y_t -= 1
            pole[y_t][x_t] = '^'
        if d_t == 'a':
            x_t -= 1
            pole[y_t][x_t] = '<'
        if d_t == 's':
            y_t += 1
            pole[y_t][x_t] = 'v'
        if d_t == 'd':
            x_t += 1
            pole[y_t][x_t] = '>'


d_s = 0
d_t = 0
is_shooted = False


def shoot():
    global d_s
    global is_shooted
    global y_s
    global x_s
    if is_shooted == True:
        if str(pole[y_s][x_s]) not in '<>^v':
            pole[y_s][x_s] = 0
        if d_s == 'w':
            y_s -= 1
        if d_s == 'a':
            x_s -= 1
        if d_s == 'd':
            x_s += 1
        if d_s == 's':
            y_s += 1
        if 0 <= x_s < 5 and 0 <= y_s < 5 :
            pole[y_s][x_s] = '+'
        else:
            is_shooted = False


def update():
    shoot()
    move()
        #time.sleep(0.1)


def printed():
    print('', *pole[0], '\n', *pole[1], '\n', *pole[2], '\n', *pole[3], '\n', *pole[4], '\n')
        #time.sleep(0.5)

printed()
while True:
    is_moving = False
    a = input('Введите направление движения танка или нажмите кнопку выстрела: ')
    if a == "exit":
        break
    elif a == "f":
        is_shooted = True
        x_s = x_t
        y_s = y_t
        d_s = d_t
    elif a:
        d_t = a
        is_moving = True
    shoot()
    move()
    printed()

    # upd_thread = threading.Thread(target=update)
    # print_thread = threading.Thread(target=printed)
    # input_thread = threading.Thread(target=vvod)
    #
    # print_thread.start()
    # input_thread.start()
    # upd_thread.start()



