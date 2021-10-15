import random


chances = 5
number = random.randint(1, 9)
print(number)
guess = int(input("Guess a Number (between 1 and 9) : "))

while chances < 5 :
    print("You lose. Better luck next time")
    
if guess == number:
    print("Congratulation! You won")
else : 
    print("You lose")

if not chances > 5 : 
    print("You lose the number is : {}".format(number))