import pygame

white = (255, 255, 255)

orange = (211, 79, 61)
mint = (9, 202, 164)
blue = (109, 192, 254)
yellow = (255, 255, 0)

grey = (59, 59, 59)

light_green = (0, 215, 0)
dark_green = (0, 153, 0)

light_red = (200, 0, 0)
dark_red = (150, 0, 0)


# returns which box was chosen
def click_pos(mouse) :
	for select_event in pygame.event.get() :

		if select_event.type == pygame.QUIT :
			pygame.quit()

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 80 <= mouse[0] <= 297 and 125 <= mouse[1] <= 322 :
				return 1

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 80 <= mouse[0] <= 297 and 322 <= mouse[1] <= 519 :
				return 4

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 80 <= mouse[0] <= 297 and 519 <= mouse[1] <= 716 :
				return 7

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 297 <= mouse[0] <= 514 and 125 <= mouse[1] <= 322 :
				return 2

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 297 <= mouse[0] <= 514 and 322 <= mouse[1] <= 519 :
				return 5

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 297 <= mouse[0] <= 514 and 519 <= mouse[1] <= 716 :
				return 8

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 514 <= mouse[0] <= 731 and 125 <= mouse[1] <= 322 :
				return 3

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 514 <= mouse[0] <= 731 and 322 <= mouse[1] <= 519 :
				return 6

		if select_event.type == pygame.MOUSEBUTTONDOWN :
			if 514 <= mouse[0] <= 731 and 519 <= mouse[1] <= 716 :
				return 9


# creates game board box on screen
def box(screen) :
	pygame.draw.line(screen, white, [50 + 30, 105 + 20], [700 + 31, 105 + 20], 5)  # top
	pygame.draw.line(screen, white, [50 + 30, 696 + 20], [700 + 31, 696 + 20], 5)  # bottom
	pygame.draw.line(screen, white, [50 + 30, 105 + 20], [50 + 30, 696 + 20], 5)  # left
	pygame.draw.line(screen, white, [700 + 31, 105 + 20], [700 + 31, 696 + 20], 5)  # right
	pygame.draw.line(screen, white, [514, 105 + 20], [514, 696 + 20], 5)  # middle_right
	pygame.draw.line(screen, white, [297, 105 + 20], [297, 696 + 20], 5)  # middle_left
	pygame.draw.line(screen, white, [50 + 30, 302 + 20], [700 + 31, 302 + 20], 5)  # middle_top
	pygame.draw.line(screen, white, [50 + 30, 499 + 20], [700 + 31, 499 + 20], 5)  # middle_bottom


# creates cross shape
def cross_shape(x1, y1, x2, y2, screen) :
	pygame.draw.line(screen, orange, [x1, y1], [x2, y2], 20)
	pygame.draw.line(screen, orange, [x1, y2], [x2, y1], 20)


# creates circle shape
def circle_shape(x, y, screen) :
	pygame.draw.circle(screen, mint, [x, y], 85, 15)


# puts cross  in correct place
def put_cross(pos, screen) :
	if pos == 1 :
		cross_shape(100, 145, 277, 302, screen)
	if pos == 2 :
		cross_shape(317, 145, 494, 302, screen)
	if pos == 3 :
		cross_shape(534, 145, 711, 302, screen)
	if pos == 4 :
		cross_shape(100, 342, 277, 499, screen)
	if pos == 5 :
		cross_shape(317, 342, 494, 499, screen)
	if pos == 6 :
		cross_shape(534, 342, 711, 499, screen)
	if pos == 7 :
		cross_shape(100, 539, 277, 696, screen)
	if pos == 8 :
		cross_shape(317, 539, 494, 696, screen)
	if pos == 9 :
		cross_shape(534, 539, 711, 696, screen)


# puts circle in correct place
def put_circle(pos, screen) :
	if pos == 1 :
		circle_shape(188, 223, screen)
	if pos == 2 :
		circle_shape(405, 223, screen)
	if pos == 3 :
		circle_shape(620, 223, screen)
	if pos == 4 :
		circle_shape(188, 420, screen)
	if pos == 5 :
		circle_shape(405, 420, screen)
	if pos == 6 :
		circle_shape(620, 420, screen)
	if pos == 7 :
		circle_shape(188, 617, screen)
	if pos == 8 :
		circle_shape(405, 617, screen)
	if pos == 9 :
		circle_shape(620, 617, screen)


# puts text on screen
def put_text(word, x, y, font, screen, color) :
	text = font.render("{}".format(word), True, color)
	return screen.blit(text, (x, y))


# takes keyboard input from user
def inpt(player, screen, title_font, normal_font, text) :
	screen.fill(grey)
	put_text('Tic Tac Toe', 285, 50, title_font, screen, blue)
	put_text("____________", 282, 55, normal_font, screen, blue)
	word = ""
	if text == "g":
		name_qn = "Enter P" + str(player) + " name: "
	else:
		name_qn = "Enter username to check: "
	put_text(name_qn, 150, 400, normal_font, screen, yellow)
	pygame.display.update()
	done = True
	while done :
		for event1 in pygame.event.get() :
			if event1.type == pygame.QUIT :
				pygame.quit()
			if event1.type == pygame.KEYDOWN :
				word += event1.unicode
				if event1.key == pygame.K_BACKSPACE :
					word = word[0 : len(word) - 2]
					pygame.draw.rect(screen, grey, pygame.Rect(150, 450, 550, 550))
				if event1.key == pygame.K_RETURN or event1.key == pygame.K_KP_ENTER:
					done = False
			put_text(word, 150, 450, normal_font, screen, white)
			pygame.display.update()

	return word.capitalize()

