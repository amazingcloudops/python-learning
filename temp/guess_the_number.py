import random
print("What's your name: ")
name = input()

print("Nice to meet you " + str(name) + ". Let's play a game")
print("I have a number in my mind, let's see if you can guess!")

secretNumber = random.randint(1,20)
#print (secretNumber)

for guess_attempt in range(1,7):
    user_guess=input("Enter the number that you guess: ")
    if int(user_guess) < secretNumber:
        print("The number entered is too low")
    elif int(user_guess) > secretNumber:
        print("The number entered is too high")
    else:
        print("You got it right in "+ str(guess_attempt) + " attempts")
        break