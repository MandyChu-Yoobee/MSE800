import random

# Define the card pool
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    """Randomly pick one card from the unlimited deck"""
    return random.choice(cards)

def calculate_score(hand):
    """Calculate hand value, handle Ace (11 or 1) logic"""
    total = sum(hand)
    # If bust and ace(11) exists, turn ace into 1
    if total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total

def blackjack_game():
    player_hand = []
    dealer_hand = []

    # Deal initial 2 cards for player and dealer
    for _ in range(2):
        player_hand.append(draw_card())
        dealer_hand.append(draw_card())

    game_over = False

    # Player turn
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"\nYour cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 21 or player_score > 21:
            game_over = True
        else:
            draw_more = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if draw_more == "y":
                player_hand.append(draw_card())
            else:
                game_over = True

    # Dealer's turn: dealer must draw until score >=17
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(draw_card())

    final_player = calculate_score(player_hand)
    final_dealer = calculate_score(dealer_hand)

    print(f"\nYour final hand: {player_hand}, final score: {final_player}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {final_dealer}")

    # Game result logic
    if final_player > 21:
        print("You went over 21. You lose!")
    elif final_dealer > 21:
        print("Dealer bust! You win!")
    elif final_player == final_dealer:
        print("Draw!")
    elif final_player > final_dealer:
        print("You win!")
    else:
        print("You lose!")

# Start the game
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    blackjack_game()

print("Thanks for playing!")
