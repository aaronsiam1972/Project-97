import random
print("Guess The Number")
#randint function to generate numbers random between 1-9
number = random.randint(1,9)
chances = 0
print("Guess the number between 1 and 9")
while chances < 5:
    guess = int(input("Enter your guess"))

#compare the user entered number by the number guessed by system
    if guess == number: 
      print("Congratulations You Won")
      break
    elif guess<number:
      print("You number was too low, guess a higher number than", guess)
    else:
      print("Your number was too high, guess a number lower than", guess)
    chances += 1
if not chances<5:
    print("You Lose, The number is ", number)
    