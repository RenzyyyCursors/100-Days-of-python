#%%
import random

player = []
you = []
you_total_value = 0
player_total_value = 0

def deal_card():
    cards = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"K":10,"Q":10,"J":10}
    selected_card,card_value = random.choice(list(cards.items()))
    return selected_card,card_value

def player_move(player,player_total_value):
    player_card ,player_value = deal_card() 

    if player_total_value < 17:    
        player.append(player_card)
        player_total_value += player_value 
    else:
        stand = random.choice([True, False])
        if not stand:
            player.append(player_card)
            player_total_value += player_value   

    return player_total_value
while True:
    user_in = input("Press Enter to start or (q) to quit")
    if user_in.lower() == 'q':
        print("Thanks for Playing.")
        break

    for i in range(2):
        pcard_name , pcard_value = deal_card()
        player.append(pcard_name)
        player_total_value += pcard_value

        ycard_name , ycard_value = deal_card()
        you.append(ycard_name)
        you_total_value += ycard_value

    temp = player[:]
    temp[1] = "*"
    print(f"Your cards: {you},Players cards: {temp}")

    while player_total_value < 22 and you_total_value < 22:
        if player_total_value == you_total_value == 21:
            print("Draw Game")
            break
        if player_total_value == 21:
            print("Player won!")
            break
        if you_total_value == 21:
            print("You won!")
            break 

        hit_stand = input("(h) for hit and (s) for stand")
        if hit_stand.lower() == 's':
            player_total_value = player_move(player, player_total_value)
            continue

        elif hit_stand.lower() == 'h':
            you_card ,you_value = deal_card()
            you.append(you_card)
            you_total_value += you_value
            player_total_value = player_move(player, player_total_value)

        print(you,player)

    if player_total_value>21:
        print("You lose!")
        break
    if you_total_value>21:
        print("You win!")
        break
    

    




# %%
