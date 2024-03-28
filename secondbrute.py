from itertools import permutations as perm
from random import shuffle

# permutation of possible attempts: 6! or 720
# max number of attempts wont go beyond 720
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
		
print(f'{x} <- cheat ans')

print(empty_list)
print(f'{count} attempts')
