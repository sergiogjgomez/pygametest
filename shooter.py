# https://www.youtube.com/watch?v=jrUJ8EsnctI
import pygame, random

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WITHE = (255, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0 

	def update(self):
		self.speed_x = 0 
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -10
		if keystate[pygame.K_RIGHT]:	
			self.speed_x = 10
		self.rect.x += self.speed_x
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

running = True
while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	all_sprites.update()

	screen.fill(BLACK)

	all_sprites.draw(screen)

	pygame.display.flip()
pygame.quit()