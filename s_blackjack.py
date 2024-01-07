import random

# basic formatting
hand = []
dealer = []
deck = []
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

# creation of deck / deck shuffle
for suit in suits:
    for rank in ranks:
        deck.append("{} of {}".format(rank, suit))

random.shuffle(deck)


# deal the cards 
def dealCards(deck, hand):
    card = deck.pop()
    hand.append(card)
    
    
# calculate the total of each hand
def calculateTotal(hand):
    value = 0
    aceValue = False
    
    for s in hand:
        subTotal = s.split()[0]
        if subTotal.isdecimal():
            value += int(subTotal)
        elif subTotal in ["Jack", "Queen", "King"]:
            value += 10
        elif "Ace" in subTotal:
            aceValue = True 
            value += 11

    if aceValue and value > 21:
        value -= 10

    return value


# game loop
def gameLoop():
    dealCards(deck, hand)
    dealCards(deck, hand)
    dealCards(deck, dealer)
    dealCards(deck, dealer)

    while True:
        print("Your hand: {} (Total: {})".format(hand, calculateTotal(hand)))
        print("Dealer hand: ['{}', '<face down>']".format(dealer[0]))

        if calculateTotal(hand) > 21:
            print("\nThat's a bust! Player loses!\n")
            break
        
        cardChoice = input("\nWould you like to 'hit' or 'stand'? : ")
        print()
    
        if cardChoice == "hit":
            dealCards(deck, hand)
        elif cardChoice == "stand":
            break
        else:
            print("\nOnly input either 'hit' or 'stand', please!\n")

    print("Your hand: {} (Total: {})".format(hand, calculateTotal(hand)))
    print("Dealer hand: {} (Total: {})".format(dealer, calculateTotal(dealer)))
    
    if calculateTotal(hand) > 21:
        print("\nThat's a bust! Player loses!\n")
    elif calculateTotal(dealer) > 21:
        print("\nLucky! Dealer busts! Player Wins!\n")
    elif calculateTotal(hand) > calculateTotal(dealer):
        print("\nLucky! Player wins!\n")
    elif calculateTotal(hand) < calculateTotal(dealer):
        print("\nUnlucky! Dealer wins!\n")
    else:
        print("\nPush!\n")

# main logic
def main():
    print("\nWelcome to Blackjack!\n\nYou can choose from the following options:\n", end="")
    print("[1] - Start a new game\n[2] - Exit game\n")
    while True:
            try:
                choice = int(input("Options (1-2): ").strip())
            except (ValueError, TypeError):
                print("\nOnly input integers (1-2), please!")
            except (KeyboardInterrupt):
                print("\n\nBye!\n")
                break
            else:
                if choice == 1:
                    print()
                    gameLoop()
                    break
                elif choice == 2:
                    print("\nBye!\n")
                    break

main()
