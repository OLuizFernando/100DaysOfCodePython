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

user_answer = s.textinput(title='Guess a State', prompt='Enter the name of a state in Brazil:')

if user_answer in list(data_df.state):
    # t.goto(x=int(data_df[data_df.state == user_answer].x), y=int(data_df[data_df.state == user_answer].y))
    # t.write(data_df[data_df.state == user_answer].state, align='center', font=('Arial', 9, 'bold'))
    # s.update()
    print(data_df.loc[???])

t.mainloop()
