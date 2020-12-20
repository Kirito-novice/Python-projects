import pygame
import random

WIDTH = 720  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 60 # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MY = (255, 70, 140)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Классы
class Speed:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed = Speed(3, 4)
        self.color = pygame.Color(color)
        self.size = 10
        
        
    def update(self):
        h, s, v, a = self.color.hsva
        self.color.hsva = (h+1) % 360, s, v, a
        self.image.fill(self.color)
        self.speed.x = 0
        self.speed.y = 0
        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speed.x = -3
        if keystate[pygame.K_d]:
            self.speed.x = 3
        if keystate[pygame.K_w]:
            self.speed.y = -3
        if keystate[pygame.K_s]:
            self.speed.y = 3

        if self.rect.top < 0:
            self.rect.bottom = HEIGHT
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
        
        if self.rect.right > WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = WIDTH

        self.rect.x += self.speed.x
        self.rect.y += self.speed.y
        self.hitbox = (self.rect.left, self.rect.top, self.size, self.size)
        
    def grow(self):
        self.size += 5
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)

class Player2(Player):
    def update(self):

        self.rect.x += self.speed.x
        self.rect.y += self.speed.y
        
        if self.rect.top < 0:
            self.speed.y = 4+random.randint(1, 5)
        if self.rect.bottom > HEIGHT:
            self.speed.y = -4-random.randint(1, 5)
        
        if self.rect.right > WIDTH:
            self.speed.x = -3-random.randint(1, 5)
        if self.rect.left < 0:
            self.speed.x = 3+random.randint(1, 5)

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(MY)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 600)
        self.rect.y = random.randrange(50, 200)
        
        
point = 0
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
apples = pygame.sprite.Group()
player = Player(MY)
player2 = Player2(BLUE)
all_sprites.add(player)
all_sprites.add(player2)
for i in range(15):
    apple = Apple()
    all_sprites.add(apple)
    apples.add(apple)

running = True
while running:
    #контролируем скорость
    clock.tick(FPS)
    
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
            # Ввод процесса (события)
    # Обновление
    
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, apples, False)
    if hits:
        for hit in hits:
            hit.kill()
            point +=1
            player.grow()
            
    
    # Визуализация (сборка)
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, str(point), 18, WIDTH / 2, 10)
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()
    
