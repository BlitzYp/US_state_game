import pandas
import turtle
import csv
from time import sleep

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 900

def setup_screen(screen: turtle.Screen) -> None:
    screen.title("US states game")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgpic("./states_img.gif")
    screen.bgcolor("gray")
    screen.listen()
    screen.tracer(0)

def get_states() -> dict:
    with open("./states.csv", "r") as file:
        reader = csv.DictReader(file)
        res = {i.get("state").lower(): (int(i.get("x")), int(i.get("y"))) for i in reader}
        return res

if __name__ == "__main__":
    screen = turtle.Screen()
    data = pandas.read_csv("./states.csv")
    num_states = len(pandas.Series.to_list(data["state"]))
    states = get_states()
    correct = 0
    setup_screen(screen)
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    while True:
        screen.update()
        state = turtle.textinput(title=f"{correct}/{num_states} states guessed", prompt="Enter state").lower()
        if states.get(state):
            writer.setpos(states[state][0], states[state][1])
            writer.write(state.capitalize(), move=False, align="center", font=("Arial", 10, "normal"))
            correct += 1
        if correct == num_states:
            writer.setpos(0, SCREEN_HEIGHT / 2 - 30)
            writer.write("You got them all!", move=False, align="center", font=("Arial", 20, "normal"))
            sleep(2)
            break