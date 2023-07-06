# note-to-self : named this file random.py received error when trying to run first code -- per github because file is random.py it is shadowing random module from python -- rename file

import random

# this will give us a random number between 1-6
x = random.randint(1,6)
    # 2
# this will give use a random number between 0-1
y = random.random()
    # 0.33551386447621234

print(y)

# list -- random choice from list called myList
myList = ['rock', 'paper', 'scissors']

z = random.choice(myList)
    # rock

# shuffle
cards = [1,2,3,4,'J','K','Q']

random.shuffle(cards)
    # [4, 'J', 3, 2, 'K', 'Q', 1]

print(cards)