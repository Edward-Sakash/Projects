"""
Task 1
import random
number = random.randint(1, 10)
#print(number)

guess = -1

while(guess!= number):
    guess = input("guess the number")
    guess = int(guess)

print("You Win!")

"""
"""

#Bonus challenge
import random
number = random.randint(1, 1000)
guess = -1
guesses = 0

while(guess!= number):
    guess = input("guess the number")
    guesses = guesses +1
    guess = int(guess)
    if guess > number:
        print("Too big")
    if guess < number:
        print("Too small")     

print("You Win!", guesses)

"""

#Task 2
"""
a, b = 0, 1
count = 0
while count < 51:
    print(a)
    a, b = b, a+b
    count += 1
"""
"""

a, b = 0, 1
for i in range(51):
    print(a)
    a, b = b, a+b

"""

a = 0
b = 1
for n in range(51):
    print(a)
    a=b
    b=a+b


