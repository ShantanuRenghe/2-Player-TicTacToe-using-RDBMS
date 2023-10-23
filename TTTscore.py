import pygame
from TTTpygame import put_text, inpt
from TTTmysql import display_username

pygame.init()

width = 800
height = 850
size = width, height

blue = (109, 192, 254)
yellow = (255, 255, 0)

orange = (211, 79, 61)
mint = (9, 202, 164)

white = (225, 225, 225)

grey = (59, 59, 59)
light_grey = (75, 75, 75)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')

title_font = pygame.font.Font('freesansbold.ttf', 40)
normal_font = pygame.font.Font('freesansbold.ttf', 32)
check_name = ""

while True :

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			pygame.quit()

	screen.fill(grey)
	put_text('Tic Tac Toe', 285, 50, title_font, screen, blue)
	put_text("____________", 282, 55, normal_font, screen, blue)


	if check_name == "":
		check_name = inpt(1, screen, title_font, normal_font, 1)

	screen.fill(grey)
	put_text('Tic Tac Toe', 285, 50, title_font, screen, blue)
	put_text("____________", 282, 55, normal_font, screen, blue)

	table = display_username(check_name)
	try :
		put_text(table[0][1], 500, 375, normal_font, screen, mint)
		put_text(table[0][2], 500, 450, normal_font, screen, yellow)
		put_text(table[0][3], 500, 525, normal_font, screen, orange)
		put_text(check_name.replace("\r", ""), 325, 200, normal_font, screen, yellow)
		put_text("WINS", 200, 375, normal_font, screen, white)
		put_text("DRAWS", 200, 450, normal_font, screen, white)
		put_text("LOSSES", 200, 525, normal_font, screen, white)
	except IndexError:
		put_text(table, 250, 425, normal_font, screen, white)
	except TypeError:
		put_text(table, 250, 425, normal_font, screen, white)

	pygame.display.update()

	pygame.time.wait(3500)

	break
