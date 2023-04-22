import pandas
from turtle import Screen, Turtle

df = pandas.read_csv("50_states.csv")

states = df["state"].tolist()

states_lower = states.copy()
selected_state = ""

for items in states:
    states_lower[states.index(items)] = items.lower()


class GameLogic:

    def __init__(self):
        self.states = states
        print(states)
        self.states_lower_static = states_lower.copy()

        self.states_lower = states_lower
        print(states_lower)
        self.screen = Screen()
        self.selected_state = ""
        self.total_options = len(states)
        print(self.total_options)
        self.current_guess = 0
        self.df = df
        self.identified_states = []

    def check_answer(self):
        user_answer = self.screen.textinput(f"{self.current_guess}/{self.total_options} state",
                                            prompt="Guess the state").lower()

        if user_answer in self.states_lower and self.current_guess <= self.total_options:
            self.selected_state = self.states[self.states_lower_static.index(user_answer)]
            print(self.selected_state)
            loc = self.df[self.df.state == self.selected_state]

            coordinates_x = loc["x"].values[0]
            coordinates_y = loc["y"].values[0]
            location = (coordinates_x, coordinates_y)
            self.display_state(self.selected_state, location)
            self.states_lower.remove(self.selected_state.lower())
            self.identified_states.append(user_answer.title())
            self.current_guess += 1

            if self.current_guess > self.total_options:
                location = (0, 0)
                self.display_state("You Win", location)
                return False

            return True

        elif user_answer == "exit":
            missed_states = [state for state in self.states if state not in self.identified_states]
            pandas.DataFrame(missed_states).to_csv("missedstates.csv")
            return False

        return True

    def display_state(self, state, location):
        name = Turtle()
        name.hideturtle()
        name.penup()
        name.color("black")
        name.goto(location)
        name.write("\n•\n")
        name.write(state, move=True, align="center", font=("courier", 10, "normal"))

        print(self.total_options)
