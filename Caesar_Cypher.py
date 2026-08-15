# %%
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(strings,shift,decrypt):
    s = ""
    if decrypt == True:
        shift = shift *(-1)
    string = strings.lower()
    for i in range(len(string)):
        if string[i] == " ":
            s += ' '
            continue
        idx = (alphabet.index(string[i])+shift)%25
        s += alphabet[idx]
    if decrypt:
        return("Decypted: "+ s)
    return("Encrypted: "+ s)

code = input("Enter code: ")
num = int(input("Enter shift value: "))
dec = input("Do you wanna decrypt ? Press (Y) if yes and (N) if not.")
if dec.lower() == 'y':
    print(caesar(code,num,True))
elif dec.lower() == 'n':
    print(caesar(code,num,False))


# %%
