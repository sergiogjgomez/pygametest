import pygame
pygame.init()

#colores y tamaño
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,255,0)
width = 800
height = 600
screen_size = (width,height)
player_width = 15
player_heigth = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#Coordenadas y speed del player1
play1_x_coor = 50
play1_y_corr = height/2
play1_y_speed = 0

#Coordenadas y speed del player2
play2_x_coor = width - play1_x_coor - player_width
play2_y_corr = height/2
play2_y_speed = 0

#Coordenadas de la pelota
pelota_x = width/2
pelota_y = height/2
pelota_speed_x = 3
pelota_speed_y = 3

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			#Play1
			if event.key == pygame.K_w:
				play1_y_speed = -8
			if event.key == pygame.K_s:
				play1_y_speed = 8
			#Play2
			if event.key == pygame.K_UP:
				play2_y_speed = -8
			if event.key == pygame.K_DOWN:
				play2_y_speed = 8
		if event.type == pygame.KEYUP:
			play1_y_speed = 0
			play2_y_speed = 0

	if pelota_y > height or pelota_y < 10:
		pelota_speed_y *= -1
	if pelota_x > width or pelota_x < 0:
		pelota_x = width/2
		pelota_y = height/2
		pelota_speed_x *= -1
		pelota_speed_y *= -1

	if play1_y_corr < 0:
		play1_y_corr = 0
	if play1_y_corr > height-100:
		play1_y_corr = height-100 

	if play2_y_corr < 0:
		play2_y_corr = 0
	if play2_y_corr > height-100:
		play2_y_corr = height-100

	#Modificacion de coordenadas para los players y pelota
	play1_y_corr += play1_y_speed
	play2_y_corr += play2_y_speed

	#Movimiento pelota
	pelota_x += pelota_speed_x
	pelota_y += pelota_speed_y

	screen.fill(black)
	# vvvv Zona dibujo
	play1 = pygame.draw.rect(screen, blue, (play1_x_coor, play1_y_corr, player_width, player_heigth))
	play2 = pygame.draw.rect(screen, red, (play2_x_coor, play2_y_corr, player_width, player_heigth))
	pelota = pygame.draw.circle(screen, white, (pelota_x,pelota_y), 10)
	# ^^^^ Zona dibujo

	#Colisiones
	if pelota.colliderect(play1) or pelota.colliderect(play2):
		pelota_speed_x *= -1

	#Actualizacion 
	pygame.display.flip()
	clock.tick(60)

pygame.quit()