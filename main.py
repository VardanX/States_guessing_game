#Graphic part with turtle
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#below is the code for getting co-ordinates if you click on any point in the image.
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
score = 0

correct_guess = []
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

while len(correct_guess) < 50:
    answer_state = screen.textinput(title = f"({len(correct_guess)} / 50 states correct)",
                                    prompt ="What's another states name?").title()
    if answer_state == "Exit":
        states_to_learn = []
        for states in states_list:
            if states not in correct_guess:
                states_to_learn.append(states)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    elif answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_guess.append(answer_state)



