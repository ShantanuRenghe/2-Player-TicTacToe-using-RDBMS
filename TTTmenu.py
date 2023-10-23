import pygame
from TTTpygame import put_text

pygame.init()

width = 800
height = 850
size = width, height

orange = (211, 79, 61)
amethyst = (143, 78, 194)
mint = (7, 158, 140)

blue = (109, 192, 254)
yellow = (255, 255, 0)

grey = (59, 59, 59)
light_grey = (75, 75, 75)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')

title_font = pygame.font.Font('freesansbold.ttf', 40)
normal_font = pygame.font.Font('freesansbold.ttf', 32)

while True :

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			pygame.quit()

	screen.fill(grey)
	put_text('Tic Tac Toe', 285, 50, title_font, screen, blue)
	put_text("____________", 282, 55, normal_font, screen, blue)

	mouse = pygame.mouse.get_pos()

	if 340 <= mouse[1] <= 400 and 100 <= mouse[0] <= 375 :
		pygame.draw.rect(screen, orange, [100, 340, 275, 60])
	else :
		pygame.draw.rect(screen, light_grey, [100, 340, 275, 60])

	if 425 <= mouse[1] <= 485 and 250 <= mouse[0] <= 565 :
		pygame.draw.rect(screen, amethyst, [250, 425, 315, 60])
	else :
		pygame.draw.rect(screen, light_grey, [250, 425, 315, 60])

	if 340 <= mouse[1] <= 400 and 440 <= mouse[0] <= 715 :
		pygame.draw.rect(screen, mint, [440, 340, 275, 60])
	else :
		pygame.draw.rect(screen, light_grey, [440, 340, 275, 60])

	put_text("Play game", 150, 355, normal_font, screen, yellow)
	put_text("Check user", 485, 355, normal_font, screen, yellow)
	put_text("Top scores", 320, 440, normal_font, screen, yellow)

	pygame.display.update()

	for select_event in pygame.event.get() :
		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 340 <= mouse[1] <= 400 and 100 <= mouse[0] <= 375 :
				import TTTgame
				pygame.quit()
			if 340 <= mouse[1] <= 400 and 440 <= mouse[0] <= 725 :
				import TTTscore
				pygame.quit()
			if 425 <= mouse[1] <= 485 and 250 <= mouse[0] <= 565 :
				import TTThighscore
				pygame.quit()
	pygame.display.update()
