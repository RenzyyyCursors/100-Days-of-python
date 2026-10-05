#%%
tot = 0
def calc(n1,n2,ops): 
# If else tree of all operations
    if ops =='+':
        tot = n1+n2
    if ops =='-':
        tot = n1-n2
    if ops =='*':
        tot = n1*n2
    if ops =='/':
        tot = n1/n2
    if ops =='^':
        tot = n1^n2
    if ops =='%':
        tot = n1%n2
    return tot

clear = 'y'
first = True 
while True:
    userin = input("Enter to begin or (q) to quit")

    # break statement
    if userin.lower() == 'q':
        break

    # checking if first time (if so two arguments are passed)
    if not first:
        clear = input("Clear answer?. (Y) for yes (N) for No")
        
    ops = input("Input Operation [+,-,*,/,^,%]")

    # one argument with prev addition
    if clear.lower() == 'n':
        n3 = int(input("Next Number: "))
        tot = calc(tot,n3,ops)
        print(tot)

    # two addition method   
    elif clear.lower() == 'y':
        n1 = int(input("1st Number: "))
        n2 = int(input("2nd Number: "))
        tot = 0
        tot = calc(n1,n2,ops)
        print(tot)
    first = False





# %%
