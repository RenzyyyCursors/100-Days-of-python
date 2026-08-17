#%%
tot = 0
def addition(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
def exponent(n1,n2):
    return n1**n2
def modulus(n1,n2):
    return n1%n2

while True:
    userin = input("Enter to begin or (q) to quit")
    if userin.lower() == 'q':
        break
    ops = input("Input Operation [+,-,*,/,^,%] or clear(c)")
    if ops.lower() == 'c':
        tot = 0
    n1 = int(input("1st Number"))
    n2 = int(input("2nd Number"))
    if ops == '+':
        tot == addition(tot,n2)
    elif ops == '-':
        tot == subtract(tot,n2)
    



