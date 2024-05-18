import pygame
import random
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Game")
icon = pygame.image.load('spaceship.png')
player_img = pygame.image.load('player.png')
bg = pygame.image.load('bg_space.jpg')
alien = pygame.image.load('alien.png')
scaled_bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
player_x = 350
player_y = 400
change_x = 0
alien_speed = 0
alien_speed += 5
enemy_x = 0
pygame.display.set_icon(icon)
class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load('laser.png')
    def draw(self, screen):
        screen.blit(self.img, (self.x + 64, self.y))

    def move(self, speed):
        self.y -= speed
class SpaceShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_img = None
        self.laser_img = None
        self.lasers = []

    def draw(self, screen):
        screen.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(screen)

    def shoot(self):
        laser = Laser(self.x, self.y)
        self.lasers.append(laser)

    def move_lasers(self, speed):
        for laser in self.lasers:
            laser.move(speed)

class Player(SpaceShip):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = player_img

class Enemy(SpaceShip):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = alien
    def move(self, speed):
        self.y += speed

def main(change_x):
    print(change_x)
    running = True
    FPS = 60
    player = Player(350, 400)
    print(player.x)
    print(player.y)
    aliens = []
    clock = pygame.time.Clock()
    def redraw():
        screen.blit(scaled_bg, (0,0))
        player.draw(screen)
        for alien in aliens:
            alien.draw(screen)
        pygame.display.update()
    def checkWall(player_x):
        if player_x != None:
            if player_x > WIDTH - 128:
                return WIDTH - 128
            if player_x < 0:
                return 0
        return player_x
    while running:
        clock.tick(FPS)
        if len(aliens) == 0:
            for i in range(8):
                alien = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100))
                aliens.append(alien)
        for alien in aliens:
            alien.move(1)
        redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    change_x = -5
                if event.key == pygame.K_d:
                    change_x = 5
                if event.key == pygame.K_SPACE:
                    player.shoot()
            if event.type == pygame.KEYUP:
                change_x = 0
        player.x += change_x
        player.x = checkWall(player.x)
        player.move_lasers(10)
main(change_x)
