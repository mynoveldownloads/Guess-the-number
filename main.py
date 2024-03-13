from random import shuffle

class Game:
	
	def __init__(self):
		self.ans = [str(i) for i in range(1, 7)]
		shuffle(self.ans)
		print(f'{self.ans} <- cheat answer')
		
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


class Loop:
	
	def __init__(self):
		self.option = [self.game_option('y')]
		self.points = 0
		
	def win_game(self):
		self.points += 100
		print(f'\nYou now have {self.points} points')
		
	def game_option(self, option):
		
		match option:
			case 'y':
				return 'True'
			case 'Y':
				return 'True'
			case 'n':
				return 'False'
			case 'N':
				return 'False'
			case other:
				print('\nchoose y to continue the game or n to exit the game\n')
				return 'other'
				
	def game_loop(self):
		
		while 'True' in self.option:
			
			self.option.clear()
			Game()
			
			self.win_game()
			user_option = input('Would you like to continue? [y/n] ')
			self.option.append(self.game_option(user_option))
			
			
			while 'other' in self.option:
				
				self.option.clear()
				user_option2 = input('Would you like to continue? [y/n] ')
				self.option.append(self.game_option(user_option2))
			
		else:
			print('Game exited')

def main():
	
	print('Guess the number from 1 to 6')
	
	game = Loop()
	game.game_loop()
	
	
if __name__ == '__main__':
	main()
