import pygame
import random

WIDTH = 1200
HEIGHT = 700
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, speed_x, speed_y, koord_x, koord_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((x, y))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (koord_x, koord_y)
        self.speed_x = speed_x
        self.speed_y = speed_y


    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right >= WIDTH:
            self.speed_x = - self.speed_x
            self.rect.right = WIDTH - 1
        if self.rect.left <= 0:
            self.speed_x = - self.speed_x
            self.rect.left = 1
        if self.rect.bottom >= HEIGHT:
            self.speed_y = - self.speed_y
            self.rect.bottom = HEIGHT - 1
        if self.rect.top <= 0:
            self.speed_y = - self.speed_y
            self.rect.top = 1


    def set_speed(self, x, y):
        self.speed_x = x
        self.speed_y = y

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KVADRAT")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player(RED, 50, 50, 0, 0, 100, 100)
all_sprites.add(player)
player2 = Player(GREEN, 100, 100, random.randint(0, 10), random.randint(0, 10), 500, 500)
all_sprites.add(player2)
mobs_sprites = pygame.sprite.Group()
mobs_sprites.add(player2)
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False
    if left_pressed:
        player.set_speed(player.speed_x - 1, 0)
    elif right_pressed:
        player.set_speed(player.speed_x + 1, 0)
    elif up_pressed:
        player.set_speed(0, player.speed_y - 1)
    elif down_pressed:
        player.set_speed(0, player.speed_y + 1)
    else:
        player.set_speed(0, 0)

    # Обновление
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, mobs_sprites, False)
    for mob in hits:
        mob.set_speed(5, 5)


#   Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
