# Nine Boxes on a Board.
a1 = " " 
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "

# Input from User as "inNum" and a "winCheck" variable for Win or Draw check. 
inNum = 0
winCheck = 0

# Two customized function first to print the Grid and second to check 
# If the box selectes by player is legitimate or not.
def printBoard():
	print("+ - + - + - +")

	print('|', end = ' ')
	print(a1, end = ' ')
	print("|", end = ' ')
	print(a2, end = ' ')
	print("|", end = ' ')
	print(a3, end = ' ')
	print("|")

	print("+ - + - + - +")

	print('|', end=' ')
	print(b1, end = ' ')
	print("|", end=' ')
	print(b2, end = ' ')
	print("|", end=' ')
	print(b3, end = ' ')
	print("|")

	print("+ - + - + - +")

	print('|', end=' ')
	print(c1, end = ' ')
	print("|", end=' ')
	print(c2, end = ' ')
	print("|", end=' ')
	print(c3, end = ' ')
	print("|")

	print("+ - + - + - +")
def authenticate(inNum):
	if inNum > 9 or inNum < 1:
		print("Please Enter valid Number between 1 - 9")
		return 0
	if inNum == 1:
		if a1 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	elif inNum == 2:
		if a2 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	elif inNum == 3:
		if a3 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	elif inNum == 4:
		if b1 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	elif inNum == 5:
		if b2 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	elif inNum == 6:
		if b3 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	elif inNum == 7:
		if c1 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	elif inNum == 8:
		if c2 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	elif inNum == 9:
		if c3 != " ":
			print("Please enter another number. This box is already taken")
			return 0
	return 1

# Print empty board first before start the Game.	
printBoard()

# Starting Logic Here.........

# for loop to get input. This will run 9 times for 9 boxes.
for x in range(9):
	# This is if condition to alternate players turn by using even odd logic.
	if (x % 2) == 0:
		print("Player 1 Turn. Please select your Box........")
		inNum = int(input("Enter a number: "))
		#This while is to get authentic input from the player. It will run until legitimate entry is entered.
		while authenticate(inNum) == 0:
			inNum = int(input("Enter a number: "))
		#This if condition to store and update the Board.
		if inNum == 1:
			a1 = "O"
			printBoard()
		elif inNum == 2:
			a2 = "O"
			printBoard()
		elif inNum == 3:
			a3 = "O"
			printBoard()
		elif inNum == 4:
			b1 = "O"
			printBoard()
		elif inNum == 5:
			b2 = "O"
			printBoard()
		elif inNum == 6:
			b3 = "O"
			printBoard()
		elif inNum == 7:
			c1 = "O"
			printBoard()
		elif inNum == 8:
			c2 = "O"
			printBoard()
		elif inNum == 9:
			c3 = "O"
			printBoard()
	else:
		print("Player 2 Turn. Please select your Box........")
		inNum = int(input("Enter a number: "))
		#This while is to get authentic input from the player. It will run until legitimate entry is entered.
		while authenticate(inNum) == 0:
			inNum = int(input("Enter a number: "))
		#This if condition to store and update the Board.
		if inNum == 1:
			a1 = "X"
			printBoard()
		elif inNum == 2:
			a2 = "X"
			printBoard()
		elif inNum == 3:
			a3 = "X"
			printBoard()
		elif inNum == 4:
			b1 = "X"
			printBoard()
		elif inNum == 5:
			b2 = "X"
			printBoard()
		elif inNum == 6:
			b3 = "X"
			printBoard()
		elif inNum == 7:
			c1 = "X"
			printBoard()
		elif inNum == 8:
			c2 = "X"
			printBoard()
		elif inNum == 9:
			c3 = "X"
			printBoard()

	#This is logical if condition to check if Player 1 has Won.
	if a1 == "O" and a2 == "O" and a3 == "O":
		winCheck = 1
		print("Player 1 Wins the Game")
		break
	elif b1 == "O" and b2 == "O" and b3 == "O":
		winCheck = 1
		print("Player 1 Wins the Game")
		break
	elif c1 == "O" and c2 == "O" and c3 == "O":
		winCheck = 1
		print("Player 1 Wins the Game")
		break
	elif a1 == "O" and b1 == "O" and c1 == "O":
		winCheck = 1
		print("Player 1 Wins the Game")
		break
	elif a2 == "O" and b2 == "O" and c2 == "O":
		winCheck = 1
		print("Player 1 Wins the Game")
		break
	elif a3 == "O" and b3 == "O" and c3 == "O":
		winCheck = 1
		print("Player 1 Wins the Game")
		break
	elif a1 == "O" and b2 == "O" and c3 == "O":
		winCheck = 1
		print("Player 1 Wins the Game")
		break
	elif a3 == "O" and b2 == "O" and c1 == "O":
		winCheck = 1
		print("Player 1 Wins the Game")
		break

	#This is logical if condition to check if Player 2 has Won.
	if a1 == "X" and a2 == "X" and a3 == "X":
		winCheck = 1
		print("Player 2 Wins the Game")
		break
	elif b1 == "X" and b2 == "X" and b3 == "X":
		winCheck = 1
		print("Player 2 Wins the Game")
		break
	elif c1 == "X" and c2 == "X" and c3 == "X":
		winCheck = 1
		print("Player 2 Wins the Game")
		break
	elif a1 == "X" and b1 == "X" and c1 == "X":
		winCheck = 1
		print("Player 2 Wins the Game")
		break
	elif a2 == "X" and b2 == "X" and c2 == "X":
		winCheck = 1
		print("Player 2 Wins the Game")
		break
	elif a3 == "X" and b3 == "X" and c3 == "X":
		winCheck = 1
		print("Player 2 Wins the Game")
		break
	elif a1 == "X" and b2 == "X" and c3 == "X":
		winCheck = 1
		print("Player 2 Wins the Game")
		break
	elif a3 == "X" and b2 == "X" and c1 == "X":
		winCheck = 1
		print("Player 2 Wins the Game")
		break




# This is to declare draw only if nobody won.
if winCheck == 0:
	print("Gane Draw!")
