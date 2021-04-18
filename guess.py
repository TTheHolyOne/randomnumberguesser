import random
import time
print('Welcome to number guesser!\nHave fun!')
numgen = random.randrange(1,100)
guesses = 0
while True:
	time.sleep(1)
	i = input('Please choose number through 1-100 otherwise enter q to quit or enter p to reset\n')
	while not (i.lower() in ['p', 'q'] or i.isdigit() and 0 < int(i) < 100):
		i = input('Please enter Q to quit or 1-100 \n')
	if i.lower() == 'q':
		break
	if i.lower() == 'p':
		numgen = random.randrange(1,100)
		guesses = 0
		continue

	if int(i) == numgen:
		time.sleep(1)
		guesses += 1
		print(f'You guessed correctly in {guesses} guesses!\nYour number was {i} and the answer is is {numgen}\n')
		guesses = 0
		numgen = random.randrange(1,100)
	elif int(i) < numgen:
		time.sleep(1)
		print(f'You guessed to low\nYour number you guessed was {i}')
		guesses += 1
	elif int(i) > numgen:
		time.sleep(1)
		print(f'You guessed to high\nYour number you guessed was {i}')
		guesses += 1

	

print('Shutting Down..')
