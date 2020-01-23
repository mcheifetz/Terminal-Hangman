#List of possible letters
letters = {'abcdefghijklmnopqrstuvwxyz'}

def travelToPoint(x, y):
	print(("\u001b[%s;%sf").format(str(y), str(x)))

def startGame():
	print("\u001b[8m",end='')
	print("Enter the secret phrase: ", end='')
	secretPhrase = str(input())
	print("\u001b[m",end='')
	guessedPhrase = " " * len(secretPhrase)

	startingX = 4
	while True:
		# Clear screen
		print("\u001b[2J",end='')
		# Travel to top left corner of screen
		travelToPoint(startingX, 2)
		# Turn on underscoring
		for index in range(len(secretPhrase)):
			print("\u001b[m ",end='')
			# Don't put an underscore if there is a space
			if secretPhrase[index] == " ":
				print(" ",end='')
			else:
				# Print an underscore to represent the hidden letter
				print("\u001b[4m",end='')
				# Check to see if the letter has been guessed
				if index < len(guessedPhrase) and guessedPhrase[index] != " ":
					# The letter has been guessed, write it
					print(guessedPhrase[index], end = "")
				else:
					print(" ", end='')
			print(" ", end='')
		print("\u001b[m",end='')
		# Remove underlining because done
		print("\u001b[m")
		# Ask for next letter
		letter = str(input("Enter letter: "))
		for index in range(len(secretPhrase)):
			if secretPhrase[index] == letter:
				# The letter has been guessed
				tempText = list(guessedPhrase)
				tempText[index] = letter
				guessedPhrase = "".join(tempText)
		if guessedPhrase == secretPhrase:
			print("You win!")
# Start the game
startGame()
