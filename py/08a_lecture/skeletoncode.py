import random

suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queeen', 'King']
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def create_deck():
    deck = []
    for i in range(len(suit_names)):
        for j in range(len(face_names)):
            deck.append((face_names[j], suit_names[i], value[j]))
    random.shuffle(deck)
    return deck

def hand_value(hand):
    count = 0
    ace_card = 0
    for i in range(len(hand)):
        if(hand[i][0]=='Ace'):
            ace_card = 11
        else:
            count += hand[i][2]
    if (ace_card == 11):
        if (count + ace_card <= 21):
            count += ace_card
        else:
            ace_card = 1
            count += ace_card
    return count

def card_string(card):
    return card[0] + " of " + card[1]

def ask_yesno(prompt):
    while(True):
        answer = input(prompt)
        if(answer == "y" or answer == "n"):
            break
        else:
            print("I beg your pardon")
    return True if answer == "y" else False

### Now the game start!
while (True):    
    # prompt for starting a new game and create a deck
    print ("Welcome to Black Jack!\n")
    deck = create_deck()
    
    # create two hands of dealer and player
    dealer = []
    player = []

    # initial two dealings
    card = deck.pop()
    print ("You are dealt " + card_string(card))
    player.append(card)
    card = deck.pop()
    print ("Dealer is dealt a hidden card")
    dealer.append(card)
    card = deck.pop()
    print ("You are dealt " + card_string(card))
    player.append(card)
    card = deck.pop()
    print ("Dealer is dealt " + card_string(card))
    dealer.append(card)
    print ("Your total is", hand_value(player))

    # player's turn to draw cards
    while (hand_value(player) < 21 and ask_yesno("Would you like another card? (y/n) ")):
        # draw a card for the player
        card = deck.pop()
        print ("You are dealt " + card_string(card))
        player.append(card)
        print ("Your total is", hand_value(player))
        
    # if the player's score is over 21, the player loses immediately.     
    if (hand_value(player) > 21):
        print ("You went over 21! You lost.")
    else:
        # draw cards for the dealer while the dealer's score is less than 17
        print ("\nThe dealer's hidden card was " + card_string(dealer[0]))
        while (hand_value(dealer) < 17):
            card = deck.pop()
            print ("Dealer is dealt " + card_string(card))
            dealer.append(card)
        print ("The dealer's total is", hand_value(dealer))
        
        # summary        
        player_total = hand_value(player)
        dealer_total = hand_value(dealer)
        print ("\nYour total is", player_total)
        print ("The dealer's total is", dealer_total)
        
        if (dealer_total > 21):
            print ("The dealer went over 21! You win!")
        else:
            if (player_total > dealer_total):
                print ("You win!")
            elif (player_total < dealer_total):
                print ("You lost!")
            else:
                print ("You have a tie!")
            
    if (not ask_yesno("\nPlay another round? (y/n) ")):
        break
