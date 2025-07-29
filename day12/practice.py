# Global and local scope:
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Modifying Global Scope

enemies = 1

# You can force the code allow you to modify something with global if you use the global keyword before you use it.
# It is okay to read the global scope var or use it but never modify it inside a local scope
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


import random

hard = 5
easy = 10
random_number = random.randint(1,100)
print(random_number)
def check_the_guess(number):
    if guess > random_number:
        return "too high"
    elif guess < random_number:
        return "too low"
    else:
        return 0

user = input("Enter your level: 'easy'  or 'hard' : ").lower()
if user == 'easy':
    chances = 10
else:
    chances= 5


while chances != 0 :

    guess = int(input("Guess the number: "))

    chances -=1
    if check_the_guess(guess) != 0:
        print(check_the_guess(guess))
    else:
        print("You got it right!")
        chances = 0


