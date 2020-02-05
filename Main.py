# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
  

def startGame():
	clear()
	secretPhrase = list(str(input("Enter the secret phrase: ")))
	clear()
	guessedPhrase = [" "] * len(secretPhrase)
	lives = 10
	
	while True:
		# Writing the blank word
		haveWon = True
		for index in range(len(secretPhrase)):
			# Don't put an underscore if there's a space
			if secretPhrase[index] == " ":
 				print(" ", end = " ")
			else:
				if guessedPhrase[index] == " ":
					# Print an underscore to represent the hidden letter
					# Have not won
					haveWon = False
					print("_", end = " ")
				else:
					print(guessedPhrase[index], end = " ")
		if haveWon:
			print("")
			print("You won!")
			break
		print("")
		print("")

		# Ask for next letter
		letter = str(input("Enter letter: "))
		hasLetterBeenFound = False
		count = 0
		for index in range(len(secretPhrase)):
			if secretPhrase[index] == letter:
				count = count + 1
				guessedPhrase[index] = letter
				hasLetterBeenFound = True
				if count == 1:
					print("You have " + str(lives) + " lives remaining")
					
				
		
		# User didn't guess the right letter
		if not hasLetterBeenFound:
			lives = lives - 1
			if lives == 0:
				print("You literally have no life. You lost. What a loser")
				break
			print("Try a different letter")
			print("You have " + str(lives) + " lives remaining")
		
		sleep(3) 
		clear()

	print("Finished")


# Start the game
startGame()
