from itertools import permutations as perm
from random import shuffle


def brute():
	
	x = [i for i in range(1, 7)]
	shuffle(x)
	empty_list = []
	
	count = 0
	for i in perm([i for i in range(1, 7)]):
		#print(i)
		count += 1
		if list(i) == x:
			empty_list.extend(list(i))
			break
			
	return count
		
	print(f'{x} <- cheat ans')
	print(empty_list)
	print(f'{count} attempts')

def loop(sequence):
	
	count = 0
	
	one_count = 0
	seven_count = 0
	while count < sequence:
		brute()
		count += 1
		
		if brute() == 1:
			one_count += 1
		elif brute() == 720:
			seven_count += 1
	print(f'{count} successful games')
	print(f'{one_count} single attempts')
	print(f'{seven_count} 720 attempts')

loop(100)
