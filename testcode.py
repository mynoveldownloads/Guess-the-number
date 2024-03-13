from random import shuffle

class Game:
	
	def __init__(self):
		self.ans = [str(i) for i in range(1, 7)]
		shuffle(self.ans)
		print(self.ans)
		
		self.attempts = 0
		self.start_game()
	
	def check(self, input_list):
		#if [str(j) for j in range(1, 7)] == input_list and len(input_list) == 6:
		if '1' and '2' and '3' and '4' and '5' and '6' in input_list and len(input_list) == 6:
			return True
		else:
			return False
			
	def counter(self, input_list, ans):
		correct = 0
		wrong = 0
		
		if self.check(input_list) == True:
			for y in range(6):
				if input_list[y] == ans[y]:
					correct += 1
				else:
					wrong += 1
			print(f'correct: {correct}, wrong: {wrong}')
		else:
			print('Your guess must be a 6-digit number with no repetition')
	
	def start_game(self):
		
		user_guess = []
		input_1 = list(input('\nguess: '))
		
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
			
			return 'win'
			

def game_option(option):
	
	match option:
		case 'y':
			return 'continue'
		case 'Y':
			return 'continue'
		case 'n':
			return 'stop'
		case 'N':
			return 'stop'
		case other:
			print('choose y/Y to continue the game or n/N to exit the game')
			
def game_loop():
	
	game_opt = [game_option('y')]
	
	while 'continue' in game_opt:
		
		game_opt.clear()
		Game()
		
		user_option = input('Would you like to continue? [y/n] ')
		game_opt.append(game_option(user_option))
		
	else:
		print('Game exited')

def main():
	
	points = 0
	
	game_loop()
	
	
	#print(f'\nGame exited. Thanks for playing! \nCredits: \n- Game idea and raw code by me (mynov) \n- OOP code assisted with ChatGPT')

if __name__ == '__main__':
	main()
