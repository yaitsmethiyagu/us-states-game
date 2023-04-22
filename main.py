from turtle import Screen

from game_logic import GameLogic

screen = Screen()
screen.setup(height=500, width=750)
screen.bgpic("blank_states_img.gif")

game_logic = GameLogic()

is_on = True

while is_on:
    is_on = game_logic.check_answer()


screen.mainloop()
