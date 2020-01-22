#List of possible letters
letters = {'abcdefghijklmnopqrstuvwxyz'}

def travelToPoint(x, y):
	print(("\u001b[%s;%sH").format(y, x))

def startGame():
	secretPhrase = str(input("Enter the secret phrase: "))
	guessedPhrase = " " * len(secretPhrase)

	startingX = 4
	while True:
		# Clear screen
		print("\u001b[2J")
		# Travel to top left corner of screen
		travelToPoint(startingX, 2)
		# Turn on underscoring
		for index in range(len(secretPhrase)):
			# Don't put an underscore if there is a space
			if secretPhrase[index] == " ":
				print("\u001b[m ",end='')
			else:
				# Print an underscore to represent the hidden letter
				print("\u001b[4m",end='')
				# Check to see if the letter has been guessed
				if index < len(guessedPhrase) and guessedPhrase[index] != " ":
					# The letter has been guessed, write it
					print(guessedPhrase[index], end = "")
				else:
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
				tempText.insert(index, letter);
				guessedPhrase = "".join(tempText)

# Start the game
startGame()
