import pygame
pygame.init()
pygame.mixer.init()
from os import path

snd_dir = path.join(path.dirname(__file__), 'snd')
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)

walk_right = []
walk_left = []
stand = [pygame.image.load('pysto.png')]


x = 5
y = 510
widht = 45
height = 85
speed = 20
BLUE = (0, 0, 255)

jump = False
jump_count = 10
left = False
right = False

# Можно юзать переменную для проверки поворота игрока в каждую из сторон
anim_count = 0

window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Test Game')
clock = pygame.time.Clock()
pygame.mixer.music.play(loops=-1)

def draw():
    global anim_count

    if anim_count + 1 >= 30:
        anim_count = 0
    if left:
# Как это понял я: изначально, когда пользователь начинает ходьбу - его anim_count = 0 тогда первые 5 кадров будет отрисовываться 1ая картинка из списка walk_left, осле 5-ти кадров целочисленной деление и опять 5 кадров для 2-ой картинки, т.к. мы в цикле, где постоянно идет покадровое обновление.
        window.blit(walk_left[anim_count // 5], (x, y))
        anim_count += 1
    elif right:
        window.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    else:
        window.blit(stand, (x, y))

    window.blit(stand, (0, 0))
    pygame.display.update()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 1200 - widht - 10:
        x += speed
    if keys[pygame.K_SPACE]:
        jump = True
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) // 2
                jump_count -= 1
            else:
                y -= (jump_count ** 2) // 2
                jump_count -= 1
        else:
            jump = False
            jump_count = 10

    draw()

pygame.quit()

