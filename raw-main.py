from random import shuffle

ans = []

for i in range(1, 7):
	ans.append(str(i))

shuffle(ans)
#print(ans)

def guess():
	user_in = list(input('guess: '))
	
	return user_in

def check(input_list):
	if '1' and '2' and '3' and '4' and '5' and '6' in input_list and len(input_list) == 6:
		return True
	else:
		return False
		
def counter(input_list, ans):
	correct = 0
	wrong = 0
	if check(input_list) is True:
		for y in range(6):
			if input_list[y] == ans[y]:
				correct += 1
			else:
				wrong += 1
		print(f'correct: {correct}, wrong: {wrong}')
	else:
		print('nono')
	
attempts = 0
user_guess = []
guess = guess()

for x in guess:
	user_guess.append(x)

counter(guess, ans)
attempts += 1
#print(user_guess)

while user_guess != ans:
	user_guess.clear()
	user_input = list(input('guess: '))
	
	for z in user_input:
		user_guess.append(z)
	
	#print(user_guess)
	
	counter(user_input, ans)
	attempts += 1
	
else:
	user_ans = ''.join(user_guess)
	game_ans = ''.join(ans)
	
	print(f'\nYou won! \nYour guess is {user_ans} \nGame answer is {game_ans} \nTotal attempts: {attempts}')
