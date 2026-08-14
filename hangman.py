#%%
import random
max_wrong = 6
wrongtries = 0

words = ['hellow','best','letter','queens','number']

HANGMANPICS = [
    """
  +---+
      |
      |
      |
=========""",
    """
  +---+
  O   |
      |
      |
=========""",
    """
  +---+
  O   |

  |   |
      |
=========""",
    """
  +---+
  O   |
 /|   |
      |
=========""",
    """
  +---+
  O   |
 /|\\  |
      |
=========""",
    """
  +---+
  O   |
 /|\\  |
 /    |
=========""",
    """
  +---+
  O   |
 /|\\  |
 / \\  |
=========""",
]

def u_input():
    guessed = input('Enter a guess. ')
    return guessed


def randomword(words):
    word = random.choice(words)
    return word

word = randomword(words)

dislay = ''
lett = []
print(word)
while wrongtries<max_wrong:

    isCor = False
    guess = u_input()
    temp_disp = ''
    len_non = 0
    for i in word:
        if  i == guess:
            temp_disp += i
            isCor = True
        elif i in lett:
            temp_disp += i
        else:
            temp_disp += '_'
            len_non += 1

    if isCor and guess not in lett:
        lett.append(guess)
    if not isCor:
        wrongtries += 1

    guesses = max_wrong - wrongtries
    print(f"You guessed {len(lett)}/{len(word)} :{temp_disp} | Guesses left:{max_wrong- wrongtries} ")
    print(HANGMANPICS[wrongtries])

    if word == temp_disp:
        print("You won!")
        break

else:
    print("You lost!")


        
    
        




    




# %%
