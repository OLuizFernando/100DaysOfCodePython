import turtle as t
import pandas

s = t.Screen()
s.tracer(0)
s.title('Brazil States Game')
s.bgpic('map.gif')
t.penup()
t.hideturtle()

data_df = pandas.read_csv('27_states.csv')

# for i in range(len(data_df)):
#     t.goto(x=data_df.x[i], y=data_df.y[i])
#     t.write(data_df.state[i], align='center', font=('Arial', 9, 'bold'))
#     s.update()

guesses = []
score = len(guesses)

game_is_on = True
while game_is_on:

    user_answer = s.textinput(title=f'{score}/27 States Correct',
                              prompt='Enter the name of a state in Brazil:')\
                              .title().replace('Do', 'do').replace('De', 'de').replace('Df', 'DF')

    if user_answer in list(data_df.state) and user_answer not in guesses:

        guesses.append(user_answer)

        t.goto(x=int(data_df[data_df.state == user_answer].iloc[0].x),
               y=int(data_df[data_df.state == user_answer].iloc[0].y))

        index = data_df[data_df.state == user_answer].index[0]
        t.write(data_df.state[index], align='center', font=('Arial', 9, 'bold'))

        s.update()

        if score >= 27:
            game_is_on = False
