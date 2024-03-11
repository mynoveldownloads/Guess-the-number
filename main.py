"""
	[12-03-24]
	'Guess the number', a number guessing game made by mynoveldownloads
	
	How the game works:
		- guess a 6-digit number ranging from 1 to 6
		- make sure the number has no repeating digits
		- there is no attempt limit for each number
		- you will be awarded 100 points for guessing a number
		- you are given the option to continue or exit the game
		
	Credits:
		- game idea (inspired from some reddit video) by me (mynov)
		- raw code (no chatgpt) by me
		- OOP (object-oriented programming)/classes code assisted with chatgpt
"""

from random import shuffle

class Game:
	
	def __init__(self):
		"""
			Generate a random 6-digit number with no repeated digits (answer)
			
			My solution:
				- use a for loop to generate numbers 1 to 6
				- add the numbers into a list and randomise the positions of
				  the numbers in the list by using the shuffle() function
		"""
		self.ans = [str(i) for i in range(1, 7)]
		shuffle(self.ans)
		print(self.ans)
		
		
		"""
			Count the number of attempts to guess a number
			Initiate the game by executing the start_game() function
		"""
		self.attempts = 0
		self.start_game()
	
	
	"""
		Checks if the user guess (input) follows the game rules, 6-digit number,
		no digit repetition, no letters/other characters in the input
	"""
	def check(self, input_list):
		#if [str(j) for j in range(1, 7)] == input_list and len(input_list) == 6: 
		# doesnt work, only returns True if user guess is 123456, returns False for any other guesses
		
		
		"""
			My solution:
				- set an if condition such that the input only accepts the numbers
				  1 to 6 and that the length of the input is 6 characters
				- if condition to check if the numbers 1 to 6 exist in the list and
				  nothing else
				- returns True to verify that the user input has passed the checking
				  test
		"""
		if '1' and '2' and '3' and '4' and '5' and '6' in input_list and len(input_list) == 6:
			return True
		else:
			return False
	
	
	"""
		Counter function that tracks the number of correct or wrong guesses of
		the position of the digit of the user input to check if it matches the 
		index of the game answer - essentially acting as a hint
	"""
	def counter(self, input_list, ans):
		correct = 0
		wrong = 0
		
		
		"""
			My solution:
				- calls the check function (method in this case) to verify if
				  the user input is following game rules
				- once verified, use a for loop to generate the index 0 to 5
				  to check which digit was correctly guessed, but the position/
				  index of the digit will not be shown
		"""
		if self.check(input_list) is True:
			for y in range(6):
				if input_list[y] == ans[y]:
					correct += 1
				else:
					wrong += 1
			print(f'correct: {correct}, wrong: {wrong}')
		else:
			print('Your guess must be a 6-digit number with no repetition')
	
	
	"""
		Start of the game, asks the player to guess the number. Calls the above
		methods to make sure nothing goes wrong in the game. Keeps track of number
		of attempts of each guess
	"""
	def start_game(self):
		
		
		"""
			My solution:
				- set the user guess to be an empty list, values will be added
				  into the list after the user inputs the number with a for loop
				- user_guess.clear() is meant for the values of the user input in the
				  user guess list to restart every time the player makes a guessing
				  attempt to avoid duplicates or the new values stacking on top of 
				  the previous values
				- calls the counter function to count the number of correct or wrong
				  guesses
				- make a while loop with a condition such that the user guess doesnt
				  match the answer, so that the game will keep running until the 
				  player correctly guesses the number, which will no longer satisfy
				  the condition and end the game
				- outputs the user guess, game answer and number of attempts
		"""
		user_guess = []
		input_1 = list(input('guess: '))
		
		for x in input_1:
			user_guess.append(x)
		
		self.counter(user_guess, self.ans)
		self.attempts += 1
		
		while user_guess != self.ans:
			user_guess.clear()
			input_2 = list(input('guess: '))
			
			for z in input_2:
				user_guess.append(z)
			
			self.counter(user_guess, self.ans)
			self.attempts += 1
		else:
			user_ans = ''.join(user_guess)
			game_ans = ''.join(self.ans)
	
			print(f'\nYou won! \nYour guess is {user_ans} \nGame answer is {game_ans} \nTotal attempts: {self.attempts}')


"""
	Main function that determines if the game continues runnning indefinitely
	based on the player's desire to continue playing
"""
def main():
	
	
	"""
		My solution:
			- set a point system that adds 100 points every time the player correctly
			  guesses a number
			- continue_game command set as 'y' by default such that it does not
			  satisfy the while condition so that it will keep running until the
			  player decides to stop playing and answer 'n', which terminates the
			  game
	"""
	points = 0
	continue_game = ['y']
	
	while 'n' not in continue_game:
		
		Game()
		points += 100
		
		print(f'\nYou now have {points} points')
		continue_game.clear()
		ask_user = input('Would you like to continue? [y/n] ')
		continue_game.append(ask_user)
	
	print(f'\nGame exited. Thanks for playing! \nCredits: \n- Game idea and raw code by me (mynov) \n- OOP code assisted with ChatGPT')

if __name__ == '__main__':
	main()
