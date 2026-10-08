import pandas 

letter_name = pandas.read_csv('nato_phonetic_alphabet.csv')
letter_data = pandas.DataFrame(letter_name)

letter_dict = {row.letter:row.code for (index,row) in letter_data.iterrows()}
print(letter_dict)

while True:
    user = input("Enter your name. (q) to quit: ")

    try:
        if user == 'quit':
            break
        caps_user = user.upper()
        nato_list = [letter_dict[i] for i in caps_user]
        print(nato_list)
        
    except KeyError:
        print("Aplabets allowed only.")
