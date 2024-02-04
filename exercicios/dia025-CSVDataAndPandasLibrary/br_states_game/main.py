import turtle as t
import pandas

s = t.Screen()
s.tracer(0)
s.title('Brazil States Game')
s.bgpic('map.gif')
t.penup()
t.hideturtle()

data_df = pandas.read_csv('27_states.csv')

guesses = []

game_is_on = True
while game_is_on:

    try:
        user_answer = s.textinput(title=f'{len(guesses)}/27 States Correct',
                                  prompt='Enter the name of a state in Brazil:')\
                                .title().replace('Do', 'do').replace('De', 'de')\
                                .replace('Df', 'DF').replace('Distrito Federal', 'DF')

        if user_answer in list(data_df.state) and user_answer not in guesses:

            guesses.append(user_answer)

            state_data = data_df[data_df.state == user_answer]

            t.goto(x=int(state_data.x.iloc[0]), y=int(state_data.y.iloc[0]))
            t.write(state_data.state.item(), align='center', font=('Arial', 9, 'bold'))

            s.update()

            if len(guesses) >= 27:
                game_is_on = False
                print('\033[32mYou won the game.\033[m')

    except AttributeError:
        game_is_on = False
        print('\033[31mYou left the game.\033[m')

        missing_states = []
        for state in list(data_df.state):
            if state not in guesses:
                missing_states.append(state)

        print('\nThe following states were missing:')
        for state in sorted(missing_states):
            print(state)
