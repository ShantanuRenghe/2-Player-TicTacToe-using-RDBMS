import pygame
from TTTpygame import put_text
from TTTmysql import high_score

pygame.init()

width = 800
height = 850
size = width, height

blue = (109, 192, 254)
yellow = (255, 255, 0)

pos_color = ((0, 125, 101), (62, 179, 91), (255, 255, 255), (212, 110, 21), (217, 42, 33))

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

	table = high_score()

	i = 0
	while i < len(table) and i < 5:
		put_text(str(i+1) + ". " + table[i][0], 200, 300 + (75*i), normal_font, screen, white)
		put_text(table[i][1], 550, 300 + (75*i), normal_font, screen, pos_color[i])
		i += 1
	
	put_text("WINS", 520, 225, normal_font, screen, white)

	pygame.display.update()

	pygame.time.wait(3500)

	break
