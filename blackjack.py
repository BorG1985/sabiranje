import random,time
cards = 2*[i for i in range(2,15)]
cards_length = len(cards)
for i in range(cards_length): 
    random_card = random.randint(i,cards_length-1)
    tmp = cards[random_card]
    cards[random_card] = cards[i]
    cards[i] = tmp

hand = []

while cards: 
    hand.append(cards.pop()) 
    hand_sum = sum(hand)
    hand_finished = False
    if hand_sum > 21: 
        print("Bust!")
        hand_finished = True
    elif hand_sum == 21:
        if len(hand) == 2:
            print("Black Jack!")
        else:
            print("Win")
        hand_finished = True
    else:
        if hand_sum >= 16:
            print("Over limit")
            hand_finished = True
    if hand_finished:
        print(hand)
        hand.clear()
    time.sleep(1)
    
 