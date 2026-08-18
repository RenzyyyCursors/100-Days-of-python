#%%
tot = 0
def calc(n1,n2,ops,tot):
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

first = True 
while True:
    userin = input("Enter to begin or (q) to quit")
    if userin.lower() == 'q':
        break
    if 
    clear = input("Continue with current answer?. (Y) for yes (N) for No")
    ops = input("Input Operation [+,-,*,/,^,%]")
    if clear.lower() == 'n':
        n3 = int(input("Next Number: "))
        
    elif clear.lower() == 'y':
        n1 = int(input("1st Number: "))
        n2 = int(input("2nd Number: "))




