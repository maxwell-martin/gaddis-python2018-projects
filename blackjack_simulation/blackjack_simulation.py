import random

def main():
    deck = create_deck()
    run_game(deck, "Player 1", "Player 2")

def create_deck():
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    return deck

def run_game(deck, player1, player2):
    while len(deck) > 0:
        hand_value_p1 = 0
        hand_value_p2 = 0

        hand_p1 = {}
        hand_p2 = {}
        
        while hand_value_p1 < 21 and hand_value_p2 < 21:
            card = get_random_card(deck)
            value = deck.pop(card, -1)

            if card in ['Ace of Spades', 'Ace of Hearts', 'Ace of Clubs', 'Ace of Diamonds']:
                temp_hand_value_p1 = hand_value_p1
                temp_hand_value_p1 += 11
                if temp_hand_value_p1 > 21:
                    hand_value_p1 += 1
                    hand_p1[card] = 1
                else:
                    hand_value_p1 = temp_hand_value_p1
                    hand_p1[card] = 11
            else:
                hand_value_p1 += value
                hand_p1[card] = value

            if len(deck) == 0:
                display_winner(hand_value_p1, hand_value_p2, hand_p1, hand_p2)
                print()
                print("No more cards left. Simulation complete.")
                return
            
            if hand_value_p1 > 21:
                break

            card = get_random_card(deck)
            value = deck.pop(card, -1)

            if card in ['Ace of Spades', 'Ace of Hearts', 'Ace of Clubs', 'Ace of Diamonds']:
                temp_hand_value_p2 = hand_value_p2
                temp_hand_value_p2 += 11
                if temp_hand_value_p2 > 21:
                    hand_value_p2 += 1
                    hand_p2[card] = 1
                else:
                    hand_value_p2 = temp_hand_value_p2
                    hand_p2[card] = 11
            else:
                hand_value_p2 += value
                hand_p2[card] = value

            if len(deck) == 0:
                display_winner(hand_value_p1, hand_value_p2, hand_p1, hand_p2)
                print()
                print("No more cards left. Simulation complete.")
                return
            
            if hand_value_p2 > 21:
                break

        display_winner(hand_value_p1, hand_value_p2, hand_p1, hand_p2)

    print()
    print("No more cards left. Simulation complete.")

def get_random_card(deck):
    cards_dict_keys = deck.keys()
    cards = []
    for c in cards_dict_keys:
        cards.append(c)
    index = random.randint(0, len(deck) - 1)
    card = cards[index]
    return card

def get_winner(hand_value_p1, hand_value_p2):
    if hand_value_p1 == 21 and hand_value_p2 != 21:
        return "Player 1 wins"
    elif hand_value_p1 != 21 and hand_value_p2 == 21:
        return "Player 2 wins"
    elif hand_value_p1 == 21 and hand_value_p2 == 21:
        return "Tie game"
    elif hand_value_p1 < 21 and hand_value_p2 > 21:
        return "Player 1 wins"
    elif hand_value_p1 > 21 and hand_value_p2 < 21:
        return "Player 2 wins"
    else:
        return "Value of hands less than 21."

def display_winner(hand_value_p1, hand_value_p2, hand_p1, hand_p2):
    print()
    print("Player 1 Hand:", hand_p1)
    print("Player 2 Hand:", hand_p2)
    print(get_winner(hand_value_p1, hand_value_p2),
          "---","Player 1:", hand_value_p1, "|", "Player 2:", hand_value_p2)

main()
