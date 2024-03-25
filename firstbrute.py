from itertools import permutations
from random import shuffle

# very cpu intensive, might take up to 3000 attempts or more if unlucky and as little as 7 attempts

ans = [i for i in range(1, 7)]

game = [z for z in range(1, 7)]

shuffle(ans)

#print(f'game ans: {game}')

# redundant function
def check(user_input, game_ans):
    #print(user_input)
    #shuffle(user_input)
    #print(user_input)
    correct = 0
    wrong = 0
    for index in range(3):
        
        if user_input[index] == game_ans[index]:
            correct += 1
        else:
            wrong += 1
        
    print(f'correct: {correct}, wrong: {wrong}')
    if correct == 3:
        return 'True'
    else:
        return 'False'
attempts = 1
while game != ans:
    print('false')
    attempts += 1
    shuffle(game)
print(f'done. bot ans: {game}')
print(f'{ans} <- game ans')
print(f'total attempts: {attempts}')
