import pygame

from TTTdef import createBoard, getValueAtPosition, setValueAtPosition, checkIfWon
from TTTpygame import click_pos, box, put_cross, put_circle, put_text, inpt
from TTTmysql import check_user, update_result

pygame.init()

width = 800
height = 850
size = width, height

blue = (109, 192, 254)
yellow = (255, 255, 0)

grey = (59, 59, 59)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')

title_font = pygame.font.Font('freesansbold.ttf', 40)
normal_font = pygame.font.Font('freesansbold.ttf', 32)

b = createBoard(3)

p1_name = []

game = True
turns = 0

while True :

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			pygame.quit()

	p1_name = inpt(1, screen, title_font, normal_font, "g")
	p2_name = inpt(2, screen, title_font, normal_font, "g")

	check_user(p1_name)
	check_user(p2_name)

	screen.fill(grey)
	put_text('Tic Tac Toe', 285, 50, title_font, screen, blue)
	put_text("____________", 282, 55, normal_font, screen, blue)

	while game :
		p1_turn = True
		p2_turn = True
		p1_pos = 0
		p2_pos = 0

		while p1_turn :
			mouse1 = pygame.mouse.get_pos()
			box(screen)
			put_text(p1_name.strip() + "\'s Turn", 300, 775, normal_font, screen, yellow)
			player1input = click_pos(mouse1)
			if getValueAtPosition(b, player1input) == "I" :
				b = setValueAtPosition(b, player1input, "X")
				p1_pos = player1input
				p1_turn = False
			pygame.display.update()

		put_cross(p1_pos, screen)
		pygame.draw.rect(screen, grey, pygame.Rect(200, 725, 600, 100))
		pygame.display.update()
		turns += 1

		if checkIfWon(b, "X") :
			winner = "p1"
			game = False
			break

		if turns == 9 :
			winner = None
			game = False
			break

		while p2_turn :
			mouse2 = pygame.mouse.get_pos()
			box(screen)
			put_text(p2_name.strip() + "\'s Turn", 300, 775, normal_font, screen, yellow)
			player2input = click_pos(mouse2)
			if getValueAtPosition(b, player2input) == "I" :
				b = setValueAtPosition(b, player2input, "0")
				p2_pos = player2input
				p2_turn = False
			pygame.display.update()

		put_circle(p2_pos, screen)
		pygame.draw.rect(screen, grey, pygame.Rect(200, 725, 600, 800))
		pygame.display.update()
		turns += 1

		if checkIfWon(b, "0") :
			winner = "p2"
			game = False
			break

		if turns == 9 :
			winner = None
			game = False
			break

	screen.fill(grey)
	put_text('Tic Tac Toe', 285, 50, title_font, screen, blue)
	put_text("____________", 282, 55, normal_font, screen, blue)
	pygame.time.wait(1000)

	if winner == "p1" :
		put_text(p1_name.strip() + ' Wins!', 280, 375, normal_font, screen, yellow)
		update_result("w", p1_name)
		update_result("l", p2_name)
	elif winner == "p2" :
		put_text(p2_name.strip() + ' Wins!', 280, 375, normal_font, screen, yellow)
		update_result("w", p2_name)
		update_result("l", p1_name)
	else :
		put_text(' Draw !', 300, 375, normal_font, screen, yellow)
		update_result("d", p1_name)
		update_result("d", p2_name)

	pygame.display.update()

	pygame.time.wait(3500)

	break
