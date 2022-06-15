import turtle
import pandas
from score import Score

data = pandas.read_csv("50_states.csv")
state_array = []


window = turtle.Screen()
window.title("US Map Game")
image = "blank_states_img.gif"
window.addshape(image)
window.setup(width=800, height=600)
turtle.shape(image)
window.tracer(0)

score = Score()
score.update_score(len(state_array))


def create_state(x, y, name):
    new_state = turtle.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.goto(int(x), int(y))
    new_state.write(name, align="center", font=("Arial", 10, "normal"))
    state_array.append(new_state)




while True:
    input_window = turtle.textinput("State", "State")

    if len(data[data["state"] == input_window]) > 0:

        element = data[input_window == data["state"]]
        print(len(data["state"] == input_window))
        x = element["x"]
        y = element["y"]
        create_state(x, y, input_window)
        score.update_score(len(state_array))

    window.update()


