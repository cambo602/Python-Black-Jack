import random

cards = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]

p1 = 0
p1_ace = 0
p2 = 0
p2_ace = 0

start = input("Type 'Start' to begin: ")

def print_card(p1, p1_ace):
    suit = random.randint(0, 3)
    card = random.randint(0, len(cards[suit]))

    p1_total = 0

    if cards[suit][card] == 1:
        print("A")
        p1_ace += 1
        p1_total += 11
        
    if cards[suit][card] == 2:
        print("2")
        p1_total += 2

    if cards[suit][card] == 3:
        print("3")
        p1_total += 3

    if cards[suit][card] == 4:
        print("4")
        p1_total += 4

    if cards[suit][card] == 5:
        print("5")
        p1_total += 5

    if cards[suit][card] == 6:
        print("6")
        p1_total += 6

    if cards[suit][card] == 7:
        print("7")
        p1_total += 7

    if cards[suit][card] == 8:
        print("8")
        p1_total += 8

    if cards[suit][card] == 9:
        print("9")
        p1_total += 9

    if cards[suit][card] == 10:
        print("10")
        p1_total += 10

    if cards[suit][card] == 11:
        print("J")
        p1_total += 10

    if cards[suit][card] == 12:
        print("Q")
        p1_total += 10

    if cards[suit][card] == 13:
        print("K")
        p1_total += 10
        
    cards[suit].pop(card)
    
    return p1_total + p1

def print_d_card(p2, p2_ace):
    suit = random.randint(0, 3)
    card = random.randint(0, len(cards[suit]))

    p2_total = 0

    if cards[suit][card] == 1:
        print("A")
        p2_ace += 1
        p2_total += 11
        
    if cards[suit][card] == 2:
        print("2")
        p2_total += 2

    if cards[suit][card] == 3:
        print("3")
        p2_total += 3

    if cards[suit][card] == 4:
        print("4")
        p2_total += 4

    if cards[suit][card] == 5:
        print("5")
        p2_total += 5

    if cards[suit][card] == 6:
        print("6")
        p2_total += 6

    if cards[suit][card] == 7:
        print("7")
        p2_total += 7

    if cards[suit][card] == 8:
        print("8")
        p2_total += 8

    if cards[suit][card] == 9:
        print("9")
        p2_total += 9

    if cards[suit][card] == 10:
        print("10")
        p2_total += 10

    if cards[suit][card] == 11:
        print("J")
        p2_total += 10

    if cards[suit][card] == 12:
        print("Q")
        p2_total += 10

    if cards[suit][card] == 13:
        print("K")
        p2_total += 10
        
    cards[suit].pop(card)
    
    return p2_total + p2

def next_move(p1, p1_ace):
    if p1 > 21 and p1_ace > 0:
        p1 -= 10
        p1_ace -= 1
    next = input("Hit or Stand? : ")
    if next.lower() == "hit":
        print("Next Card")
        p1 = print_card(p1, p1_ace)
        print("Total")
        print(p1)
        if p1 <= 21:
            next_move(p1, p1_ace)
        else:
            game_over(p1, p2, p1_ace, p2_ace)

    elif next.lower() == "stand":
        dealer_turn(p1, p2, p2_ace)

def next_d_turn(p1, p2, p2_ace):
    if p2 > 21 and p2_ace > 0:
        p2 -= 10
        p2_ace -= 1
    if p1 >= p2 and p2 <= 18:
        print("Dealer Next Card")
        p2 = print_d_card(p2, p2_ace)
        print("Dealer Total")
        print(p2)
        if p1 >= p2 and p2 <= 18:
            next_d_turn(p1, p2, p2_ace)
        else:
            game_over(p1, p2, p1_ace, p2_ace)

    if p2 > 18:
        game_over(p1, p2, p1_Ace, p2_ace)

def game_over(p1, p2, p1_ace, p2_ace):
    if p1 > p2 and p1 < 22:
        print("You Win")
        start = input("Type 'Start' to begin: ")
        p1 = 0
        p1_ace = 0
        p2 = 0
        p2_ace = 0
        begin(start, p1)

    if p2 > p1 and p2 < 22:
        print("You Lose")
        start = input("Type 'Start' to begin: ")
        p1 = 0
        p1_ace = 0
        p2 = 0
        p2_ace = 0
        begin(start, p1, p1_ace)

    if p1 > 21:
        print("Bust You Lose")
        start = input("Type 'Start' to begin: ")
        p1 = 0
        p1_ace = 0
        p2 = 0
        p2_ace = 0
        begin(start, p1, p1_ace)

    if p2 > 21:
        print("Dealer Bust, You Win")
        start = input("Type 'Start' to begin: ")
        p1 = 0
        p1_ace = 0
        p2 = 0
        p2_ace = 0
        begin(start, p1, p1_ace)

def dealer_turn(p1, p2, p2_ace):
    print("Dealer First Card")
    p2 = print_d_card(p2, p2_ace)
    print("Dealer Second Card")
    p2 = print_d_card(p2, p2_ace)
    print("Dealer Total")
    print(p2)
    next_d_turn(p1, p2, p2_ace)

def begin(start, p1, p1_ace, cards):
    cards = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
    if start.lower() == "start":    
        
       # for i in range(len(cards)):
        #    for j in range(len(cards[i])):
         #       print(1)

        print("First Card")
        p1 = print_card(p1, p1_ace)
        print("Second Card")
        p1 = print_card(p1, p1_ace)
        print("Total")
        print(p1)
        next_move(p1, p1_ace)

    else:
        print("Invalid Input")
        start = input("Type 'Start' to begin: ")
        begin(start, p1, p1_ace)

begin(start, p1, p1_ace, cards)

while True:
    if start.lower() != start:
        print("Invalid Input")
        start = input("Type 'Start' to begin: ")
        begin(start, p1, p1_ace, cards)

    if next.lower() != stand or next.lower() != hit:
        print("Invalid Input")
        next_move(p1, p1_ace)
