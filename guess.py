import random
import os

os.system('cls')
print('Welcome to number guesser!\n')
while True:
	rannum = random.randrange(0, 101)
	i = input(f'Please choose number through 1-100 or enter q to quit\n')
	if i.lower() == 'q':
		break
	if i.lower() == 'p':
		continue
	if int(i) == rannum:
		print(f'You guessed correctly!\nThe number was {rannum}\nYou answered {i}\nEnter p to play again!\nEnter q to quit!')
		input()
	elif int(i) < rannum:
		print(f'Sorry but you too low :(\nYour guess was {i}')
		continue
		input()
	else: 
		print('Your guess is too high')
		continue
		input()
	input()

print('Shutting Down... ')