import turtle
from turtle import Turtle, Screen
from states import State, Timer

sc = Screen()
sc.setup(width=740, height=620)
sc.title("U.S. States Game")
turtle.bgpic(picname='blank_states_img.gif')

st = State()
timer = Timer(time_limit=300)  # Set game timer (e.g. 120 seconds)
timer.start()

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, 260)

game_on = True

while game_on:
    sc.update()

    # Check if timer finished before asking input
    if not timer.is_running:
        writer.clear()
        writer.write("Time is up! Game Over.", align='center', font=('Arial', 20, 'bold'))
        break

    answer_state = sc.textinput(title=f"{len(st.states)}/50 States Correct", prompt="What's another state's name? (Type 'exit' to quit)")

    # Check if user cancelled or typed exit/quit
    if answer_state is None or answer_state.lower() in ['exit', 'quit', 'q']:
        writer.clear()
        writer.write("Thanks for Playing!", align='center', font=('Arial', 20, 'bold'))
        timer.is_running = False
        break

    # Format input to Title Case (e.g. 'arkansas' -> 'Arkansas')
    guessed_state = answer_state.title()

    if guessed_state in st.states:
        writer.clear()
        writer.write("Already Guessed!", align='center', font=('Arial', 16, 'normal'))
    elif guessed_state in st.tot_list:
        writer.clear()
        writer.write("Correct!", align='center', font=('Arial', 16, 'normal'))
        st.represent(guessed_state)
        st.states.append(guessed_state)
        st.show_total()
    else:
        writer.clear()
        writer.write("State doesn't exist!", align='center', font=('Arial', 16, 'normal'))

    if len(st.states) == 50:
        writer.clear()
        writer.write("Congratulations! You guessed all 50 states!", align='center', font=('Arial', 20, 'bold'))
        timer.is_running = False
        game_on = False

sc.mainloop()