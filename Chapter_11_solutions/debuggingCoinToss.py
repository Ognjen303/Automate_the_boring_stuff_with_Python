import random, logging

logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start debuging!')

guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of guess!')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug('Start of coin toss!')
toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss:
    toss = 'heads'
else:
    toss = 'tails'

logging.debug('The coin flip resulted in: ' + str(toss))


if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')

    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
