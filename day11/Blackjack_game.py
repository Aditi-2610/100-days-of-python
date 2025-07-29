import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = []
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_total, computer_total):
    if user_total == computer_total:
        return "It's a Draw"
    elif computer_total == 0:
        return "Lose, opponent has Blackjack"
    elif user_total == 0:
        return "Win with a Blackjack"
    elif computer_total > 21:
        return "Opponent went over. You win!"
    elif user_total > 21:
        return "Lose! You went over"
    elif user_total > computer_total:
        return "You win!"
    else:
        return "You Lose!"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    user_score = -1
    computer_score = -1 # not 0 because it indicates blackjack

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, the current score is: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, the Final score is: {user_score}")
    print(f"Computer's final hand:  {user_cards}, the Final score is: {user_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower() == 'y':
    print("\n"*20)
    play_game()
