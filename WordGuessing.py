#python3
import random
import time

words = ["wall","bruno","zeni","cheeks","car","truck","spy","pokemon","digimon","dragon ball","jack","biology","english","japanese","spanish","italian"]

word = random.choice(words)

chances = len(word)*2
turn = 0
guess = ''
guesses = []
count=0

print("You've only %d chances to guess!" %(chances))

time.sleep(1)

print("Are you ready?")

time.sleep(1)

print("Go!\n")

time.sleep(1)

for letter in word:
    if letter in guesses:
        print(letter)
        count+=1
    else:
        print("_")
print()

while turn < chances:
    count=0
    guess = input("Try a letter: ")
    guesses+=guess
    for letter in word:
        if letter in guesses:
            print(letter)
            count+=1
        else:
            print("_")
    if count==chances/2:
        break
    print("%d chances remaining!\n" %(chances-turn-1))
    turn+=1

if count==chances/2:
    print("Congratulations! You win!")
else:
    print("You die!\nHahahahahah!")
    print("Word is %s!" %(word))