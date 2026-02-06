

# Display array
from game_data import data
from art import logo, vs
import random

def format_data(account):
    """format the account data into printable format"""
    account_name = account_a["name"]
    account_desc = account_a["description"]
    account_country = account_a["country"]
    print(f"{account_name}, a {account_desc}, from {account_country}")


def check_answer(user_guess, a_follower, b_follower):
    """Take a user's guess and tell which one has more followers A or B"""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    # generate a random account from game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # Ask for a guess

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" *20)
    print(logo)

    # Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # get follower of each active_count
    # use if statemtnt to check if user os correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    # GIve user feedback on their game

    if is_correct:
        score+=1
        print(f"You're right! Current score is : {score}")
    else:
        print(f"Sorry, that's wrong. Final score : {score}")
        game_should_continue = False
    # score keeping


# make the game repetable


# making account at position b bcome the account at position a

