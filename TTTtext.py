from TTTdef import createBoard, printBoard, getValueAtPosition, setValueAtPosition, checkIfWon


e = int(input("Enter size of game - "))
b = createBoard(e)
printBoard(b)

game = True

while game :
	ingame1 = True
	ingame2 = True
	while ingame1 :
		player1input = int(input("Player 1 Input - "))
		if getValueAtPosition(b, player1input) == "I" :
			b = setValueAtPosition(b, player1input, "X")
			printBoard(b)
			ingame1 = False
		else :
			print("Position already taken")
			print("Player 1, pls enter input again")
	if checkIfWon(b, "X") :
		print("Player 1 Wins !!!")
		game = False
		break
	while ingame2 :
		player2input = int(input("Player 2 Input - "))
		if getValueAtPosition(b, player2input) == "I" :
			b = setValueAtPosition(b, player2input, "0")
			printBoard(b)
			ingame2 = False
		else :
			print("Position already taken")
			print("Player 2, pls enter input again")
	if checkIfWon(b, "0") :
		print("Player 2 Wins !!!")
		game = False
