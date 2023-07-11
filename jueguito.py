# https://www.youtube.com/watch?v=xjAvXGT5z3E&list=PLuB3bC9rWQAu6cGeRo_I6QV8cz1_2V6uM&index=1
import pygame, sys, random
pygame.init()

size = (800, 500)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

#La ventana: 
screen = pygame.display.set_mode(size)
#El tiempo
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

coor_x = 10
coor_y = 10

x_speed = 0
y_speed = 0

coor_list = []
for i in range(60):
	x = random.randint(0, 800)
	y = random.randint(0, 500)
	coor_list.append([x,y])

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -5
			if event.key == pygame.K_RIGHT:
				x_speed = 5
			if event.key == pygame.K_UP:
				y_speed = -5
			if event.key == pygame.K_DOWN:
				y_speed = 5

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = 0
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0


	#pinta la pantalla
	screen.fill(white)

	#Circulos rojos
	for i in coor_list:
		pygame.draw.circle(screen, red, i, 3)
		i[1] += 0.6
		if i[1] > 500:
			i[1] = 0
	
	#Puntero Verde
	mouse_pos = pygame.mouse.get_pos()
	x = mouse_pos[0]
	y = mouse_pos[1]		
	pygame.draw.rect(screen, green, (x,y,10,10))

	#Cuadrado Azul con flechitas
	coor_x += x_speed
	coor_y += y_speed
	pygame.draw.rect(screen, blue, (coor_x, coor_y,10,10))
	if coor_x > 800: 
		coor_x = 0
	if coor_x < 0:
		coor_x = 800
	if coor_y > 500:
		coor_y = 0
	if coor_y < 0: 
		coor_y = 500

	#actualiza la pantalla y define el FPS
	pygame.display.flip()
	clock.tick(60)

