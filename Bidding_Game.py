
# %%
all_bid = {}

def bid():
    user_name = input("Enter your name: ")
    user_input = int(input("Enter the bidding amount: "))
    all_bid[user_name] = user_input

while True:
    bids = input("Do you wannt another bidder? \n Press Enter else press (Q) to quit: ")
    if bids.lower() == 'q':
        break
    print("\n"*100)
    bid()

highest = max(all_bid.values())
max_key = [key for key,val in all_bid.items() if val == highest]
for i in range(len(max_key)):
    print(f"Winner of the bidding are {max_key[i]}, bidding: {highest}")
print(f"Total bidders {len(all_bid)}")
# %%
