import random

DICE_MIN = 1
DICE_MAX = 6

print('Welcome to the dice rolling simulator!')

keep_rolling = True

while keep_rolling:
  dieOne = random.randint(DICE_MIN,DICE_MAX)
  dieTwo = random.randint(DICE_MIN,DICE_MAX)
  print('You rolled a ', dieOne, ' and a ', dieTwo,'!', sep='')

  keep_asking = True

  while keep_asking:
    roll_again = input('Would you like to roll again? (Y/N):')
    keep_asking = False if roll_again == 'N' or roll_again == 'Y' else True

  keep_rolling = False if roll_again == 'N' else True

print('Thanks for using the dice simulator!')
