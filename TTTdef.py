# creates game board
def createBoard(size) :
	board = []
	count = 1
	for i in range(size) :
		temp = []
		for j in range(size) :
			temp.append([count, "I"])
			count += 1
		board.append(temp)
	return board


# prints the game board
def printBoard(board) :
	print("----------------")
	for i in board :
		for j in i :
			print(j[1], end=" ")
		print()
	print("----------------")


# checks value at position selected
def getValueAtPosition(board, position) :
	for i in board :
		for j in i :
			if j[0] == position :
				return j[1]


# sets a value at given position
def setValueAtPosition(board, position, value) :
	for i in board :
		for j in i :
			if j[0] == position :
				j[1] = value
	return board


# checks if game is over
def checkIfWon(board, value) :
	for i in board :
		w = 0
		for j in i :
			if j[1] == value :
				w += 1
			else :
				break
		if w == len(i) :
			return True
	for i in range(0, len(board)) :
		t = 0
		for j in range(len(board)) :
			if board[j][i][1] == value :
				t += 1
			else :
				break
		if t == len(board) :
			return True
	w = 0
	for i in range(len(board)) :
		if board[i][i][1] == value :
			w += 1
		else :
			break
	if w == len(board) :
		return True
	h = 0
	i = 0
	j = len(board) - 1
	while j >= 0 :
		if board[i][j][1] == value :
			h += 1
			i += 1
			j -= 1
		else :
			break
	if h == len(board) :
		return True
	return False
