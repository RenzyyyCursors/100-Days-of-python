#%%
import random

player = []
you = []
you_total_value = 0
player_total_value = 0

# dealing card function
def deal_card():
    cards = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"K":10,"Q":10,"J":10}
    selected_card,card_value = random.choice(list(cards.items()))
    return selected_card,card_value

# player move if >17
def player_move(player,player_total_value):
    while player_total_value < 17:
        player_card, player_value = deal_card() 
        if player_card == "A" and player_total_value > 10:
            player_value = 1
        player.append(player_card)
        player_total_value += player_value 

    return player_total_value

# main function
while True:
    user_in = input("Press Enter to start or (q) to quit")
    if user_in.lower() == 'q':
        print("Thanks for Playing.")
        break

    # FIXED: Reset variables at the start of each round
    player = []
    you = []
    you_total_value = 0
    player_total_value = 0

    # first two cards
    for i in range(2):
        pcard_name , pcard_value = deal_card()
        player.append(pcard_name)
        player_total_value += pcard_value

        ycard_name , ycard_value = deal_card()
        you.append(ycard_name)
        you_total_value += ycard_value

    # show temp card
    temp = player[:]
    temp[1] = "*"
    print(f"Your cards: {you}, Players cards: {temp}")

    # Check for immediate 21 on dealing
    if player_total_value == 21 and you_total_value == 21:
        print(f"Your cards: {you} ({you_total_value}), Player cards: {player} ({player_total_value})")
        print("Draw Game")
        continue
    elif player_total_value == 21:
        print(f"Your cards: {you} ({you_total_value}), Player cards: {player} ({player_total_value})")
        print("Player won!")
        continue
    elif you_total_value == 21:
        print(f"Your cards: {you} ({you_total_value}), Player cards: {player} ({player_total_value})")
        print("You won!")
        continue

    # Users turn (Hit / Stand)
    user_standing = False
    while you_total_value < 21:
        hit_stand = input("(h) for hit and (s) for stand: ")
        if hit_stand.lower() == 's':
            user_standing = True
            break
        elif hit_stand.lower() == 'h':
            you_card, you_value = deal_card()
            if you_card == "A" and you_total_value > 10:
                you_value = 1
            you.append(you_card)
            you_total_value += you_value
            print(f"Your cards: {you} (Total: {you_total_value}), Players cards: {temp}")

    # If user busted, round ends immediately
    if you_total_value > 21:
        print(f"\nYour cards: {you} ({you_total_value}), Player cards: {player} ({player_total_value})")
        print("You lose! (Bust)")
        continue

    # Player's (Dealer's) turn after user stands
    player_total_value = player_move(player, player_total_value)

    # final printing and winner evaluation
    print(f"\nFinal Hands -> Your cards: {you} ({you_total_value}), Player cards: {player} ({player_total_value})")

    if player_total_value > 21:
        print("You win! (Player Bust)")
    elif player_total_value > you_total_value:
        print("Player won!")
    elif you_total_value > player_total_value:
        print("You win!")
    else:
        print("Draw Game")

# %%
